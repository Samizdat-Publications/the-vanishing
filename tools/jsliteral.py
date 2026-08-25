"""Parser and emitter for the JavaScript literal subset used in the-vanishing-v2.html.

The rebuild extracts case data out of a hand-authored HTML file and must be able to put
it back byte for byte. That makes this module two things at once: a parser that decodes
escapes and nothing else, and an emitter that reproduces hand-authored formatting exactly.

Three rules earn their own note, because getting any of them wrong is silent:

1. Booleans are checked before integers. In Python `isinstance(True, int)` is True, so a
   naive emitter writes `isNonDefense: 1` instead of `isNonDefense: true`. It parses, it
   runs, and the page looks identical.
2. The parser decodes escapes and performs no other normalization. Strings such as
   'phone' and 'phones' are load bearing: the behavioural edge rule is exact string
   match, so tidying them silently changes the rendered graph.
3. Apostrophe spelling is a per-block emission policy, not data. The source file uses
   three different conventions and no block mixes two.
"""

from __future__ import annotations

# Characters the source spells as escapes rather than literal bytes.
_SIMPLE_ESCAPES = {
    "n": "\n", "t": "\t", "r": "\r", "b": "\b", "f": "\f", "v": "\v",
    "0": "\0", "\\": "\\", "'": "'", '"': '"', "/": "/", "\n": "",
}

_IDENT_START = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_$")
_IDENT_CHARS = _IDENT_START | set("0123456789")


class JsParseError(ValueError):
    """Raised with a byte offset so a failure points at the source, not at a stack."""

    def __init__(self, message, text, pos):
        self.pos = pos
        line = text.count("\n", 0, pos) + 1
        col = pos - (text.rfind("\n", 0, pos) + 1) + 1
        excerpt = text[max(0, pos - 40):pos + 40].replace("\n", "\\n")
        super().__init__(
            "%s at line %d column %d (offset %d)\n  near: %s" % (message, line, col, pos, excerpt)
        )


class Parser:
    """Recursive descent over the literal subset actually present in the source.

    Supports: single and double quoted strings, bare-identifier and quoted object keys,
    arrays, objects, integers and floats, true/false/null, trailing commas, and both
    comment forms. Deliberately does not support template literals, expressions, or
    function calls, because encountering one means the assumption that a block is pure
    data has broken and the extractor should fail loudly rather than guess.
    """

    def __init__(self, text, pos=0):
        self.text = text
        self.pos = pos

    def error(self, message):
        return JsParseError(message, self.text, self.pos)

    def skip_trivia(self):
        """Consume whitespace and comments until the next meaningful character."""
        text, n = self.text, len(self.text)
        while self.pos < n:
            ch = text[self.pos]
            if ch in " \t\r\n":
                self.pos += 1
            elif text.startswith("//", self.pos):
                end = text.find("\n", self.pos)
                self.pos = n if end == -1 else end + 1
            elif text.startswith("/*", self.pos):
                end = text.find("*/", self.pos + 2)
                if end == -1:
                    raise self.error("unterminated block comment")
                self.pos = end + 2
            else:
                return

    def parse_value(self):
        self.skip_trivia()
        if self.pos >= len(self.text):
            raise self.error("unexpected end of input")
        ch = self.text[self.pos]
        if ch in "'\"":
            return self.parse_string()
        if ch == "[":
            return self.parse_array()
        if ch == "{":
            return self.parse_object()
        if ch == "-" or ch.isdigit():
            return self.parse_number()
        for word, value in (("true", True), ("false", False), ("null", None)):
            if self.text.startswith(word, self.pos):
                after = self.pos + len(word)
                if after >= len(self.text) or self.text[after] not in _IDENT_CHARS:
                    self.pos = after
                    return value
        raise self.error("unexpected token %r" % ch)

    def parse_string(self):
        quote = self.text[self.pos]
        self.pos += 1
        out = []
        text, n = self.text, len(self.text)
        while self.pos < n:
            ch = text[self.pos]
            if ch == quote:
                self.pos += 1
                return "".join(out)
            if ch == "\\":
                self.pos += 1
                if self.pos >= n:
                    raise self.error("unterminated escape")
                esc = text[self.pos]
                if esc == "u":
                    hexits = text[self.pos + 1:self.pos + 5]
                    if len(hexits) != 4:
                        raise self.error("truncated unicode escape")
                    try:
                        out.append(chr(int(hexits, 16)))
                    except ValueError:
                        raise self.error("bad unicode escape \\u%s" % hexits)
                    self.pos += 5
                    continue
                if esc == "x":
                    hexits = text[self.pos + 1:self.pos + 3]
                    if len(hexits) != 2:
                        raise self.error("truncated hex escape")
                    out.append(chr(int(hexits, 16)))
                    self.pos += 3
                    continue
                out.append(_SIMPLE_ESCAPES.get(esc, esc))
                self.pos += 1
                continue
            if ch == "\n":
                raise self.error("newline inside string literal")
            out.append(ch)
            self.pos += 1
        raise self.error("unterminated string")

    def parse_number(self):
        start = self.pos
        if self.text[self.pos] == "-":
            self.pos += 1
        while self.pos < len(self.text) and self.text[self.pos] in "0123456789":
            self.pos += 1
        is_float = False
        if self.pos < len(self.text) and self.text[self.pos] == ".":
            is_float = True
            self.pos += 1
            while self.pos < len(self.text) and self.text[self.pos] in "0123456789":
                self.pos += 1
        raw = self.text[start:self.pos]
        if raw in ("", "-"):
            raise self.error("malformed number")
        # Integers stay int so the emitter never writes 3.0 where the source has 3.
        return float(raw) if is_float else int(raw)

    def parse_array(self):
        self.pos += 1
        items = []
        while True:
            self.skip_trivia()
            if self.pos >= len(self.text):
                raise self.error("unterminated array")
            if self.text[self.pos] == "]":
                self.pos += 1
                return items
            items.append(self.parse_value())
            self.skip_trivia()
            if self.pos < len(self.text) and self.text[self.pos] == ",":
                self.pos += 1
            elif self.pos < len(self.text) and self.text[self.pos] == "]":
                self.pos += 1
                return items
            else:
                raise self.error("expected , or ] in array")

    def parse_object(self):
        self.pos += 1
        # A plain dict preserves insertion order in Python 3.7+, and key order in this
        # source is authorial rather than schematic. It is data, so it is preserved.
        obj = {}
        while True:
            self.skip_trivia()
            if self.pos >= len(self.text):
                raise self.error("unterminated object")
            if self.text[self.pos] == "}":
                self.pos += 1
                return obj
            key = self.parse_key()
            self.skip_trivia()
            if self.pos >= len(self.text) or self.text[self.pos] != ":":
                raise self.error("expected : after object key %r" % key)
            self.pos += 1
            obj[key] = self.parse_value()
            self.skip_trivia()
            if self.pos < len(self.text) and self.text[self.pos] == ",":
                self.pos += 1
            elif self.pos < len(self.text) and self.text[self.pos] == "}":
                self.pos += 1
                return obj
            else:
                raise self.error("expected , or } in object")

    def parse_key(self):
        ch = self.text[self.pos]
        if ch in "'\"":
            return self.parse_string()
        start = self.pos
        if ch not in _IDENT_START:
            raise self.error("bad object key")
        while self.pos < len(self.text) and self.text[self.pos] in _IDENT_CHARS:
            self.pos += 1
        return self.text[start:self.pos]


def parse(text, pos=0):
    """Parse one literal. Raises if trailing non-trivia remains."""
    p = Parser(text, pos)
    value = p.parse_value()
    p.skip_trivia()
    if p.pos != len(text):
        raise p.error("trailing content after literal")
    return value


def parse_prefix(text, pos=0):
    """Parse one literal and return (value, end_offset), ignoring what follows."""
    p = Parser(text, pos)
    value = p.parse_value()
    return value, p.pos


# --------------------------------------------------------------------------------------
# Emission
# --------------------------------------------------------------------------------------

# How each block spells U+2019 and the ASCII apostrophe. Verified against the source:
# no block mixes two conventions, which is what makes a per-block policy correct and a
# single global policy wrong.
APOS_U2019 = "u2019"          # PEOPLE, PRECEDENT: escape U+2019, never use \'
APOS_BACKSLASH = "backslash"  # INSTITUTIONS, PROGRAMS, ENTITY_INFO: use \' for ASCII '
APOS_SWITCH = "switch_quotes"  # PHOTOS: switch the whole string to double quotes


class Style:
    """Per-block emission policy."""

    def __init__(self, apostrophe=APOS_U2019, key_sep=": "):
        self.apostrophe = apostrophe
        self.key_sep = key_sep


def emit_string(value, style):
    """Render a Python str as a JS string literal in this block's convention."""
    if style.apostrophe == APOS_SWITCH and "'" in value:
        body = value.replace("\\", "\\\\").replace('"', '\\"')
        return '"%s"' % _escape_controls(body)

    body = value.replace("\\", "\\\\").replace("'", "\\'")
    if style.apostrophe == APOS_U2019:
        body = body.replace("’", "\\u2019")
    return "'%s'" % _escape_controls(body)


def _escape_controls(s):
    out = []
    for ch in s:
        if ch == "\n":
            out.append("\\n")
        elif ch == "\t":
            out.append("\\t")
        elif ch == "\r":
            out.append("\\r")
        else:
            out.append(ch)
    return "".join(out)


def emit_scalar(value, style):
    """Render a non-container value.

    The bool check must precede the int check. Python treats True as an int, so the
    obvious ordering emits `true` as `1`: still valid JavaScript, still renders the same
    page, and wrong in a way nothing downstream would catch.
    """
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return repr(value)
    if isinstance(value, str):
        return emit_string(value, style)
    raise TypeError("cannot emit %r" % type(value))


def emit_inline(value, style):
    """Render a value on a single line, matching the source's inline spacing.

    Inline arrays are ['a', 'b']; inline objects are { k: v, k: v }; arrays of objects
    are [{ ... }, { ... }].
    """
    if isinstance(value, list):
        return "[" + ", ".join(emit_inline(v, style) for v in value) + "]"
    if isinstance(value, dict):
        if not value:
            return "{}"
        inner = ", ".join(
            "%s%s%s" % (k, style.key_sep, emit_inline(v, style)) for k, v in value.items()
        )
        return "{ %s }" % inner
    return emit_scalar(value, style)


def scan_span(text, start):
    """Return the end offset of the balanced literal beginning at `start`.

    Unlike the parser this does not interpret the contents, so it works on blocks whose
    elements are wrapped in factory calls such as `P_({...})` or `other(...)`. Strings
    and comments are skipped so that a bracket inside prose cannot unbalance the scan.
    """
    depth = 0
    i = start
    n = len(text)
    while i < n:
        ch = text[i]
        if ch in "'\"":
            quote = ch
            i += 1
            while i < n:
                if text[i] == "\\":
                    i += 2
                    continue
                if text[i] == quote:
                    i += 1
                    break
                i += 1
            continue
        if text.startswith("//", i):
            end = text.find("\n", i)
            i = n if end == -1 else end + 1
            continue
        if text.startswith("/*", i):
            end = text.find("*/", i + 2)
            if end == -1:
                raise JsParseError("unterminated block comment", text, i)
            i = end + 2
            continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
            if depth == 0:
                return i + 1
            if depth < 0:
                raise JsParseError("unbalanced bracket", text, i)
        i += 1
    raise JsParseError("unterminated literal", text, start)
