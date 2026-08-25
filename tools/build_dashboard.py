"""data/ -> dist/the-vanishing.html

Reads the merged dataset and the shell template, emits each data block in its own
formatting convention, and splices them into the holes by position.

This never reads research/. The pipeline is research -> merge -> data -> build, and
short-circuiting it would let the build pass while merge is broken.

    python3 tools/build_dashboard.py
"""

from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import emit_blocks

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEP = "\x00HOLE\x00"


def build():
    with open(os.path.join(ROOT, "data", "dataset.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    with open(os.path.join(ROOT, "tools", "templates", "dashboard.shell.html"),
              encoding="utf-8", newline="") as fh:
        shell = fh.read()
    with open(os.path.join(ROOT, "tools", "templates", "holes.json"), encoding="utf-8") as fh:
        holes = json.load(fh)

    parts = shell.split(SEP)
    if len(parts) != len(holes) + 1:
        raise SystemExit("shell has %d holes, manifest lists %d" % (len(parts) - 1, len(holes)))

    emitters = emit_blocks.build_emitters(data)
    out = []
    for i, part in enumerate(parts):
        out.append(part)
        if i < len(holes):
            name = holes[i]["block"]
            if name not in emitters:
                raise SystemExit("no emitter registered for block %s" % name)
            out.append(emitters[name]())
    return "".join(out)


def main():
    html = build()
    os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
    path = os.path.join(ROOT, "dist", "the-vanishing.html")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(html)
    print("built dist/the-vanishing.html  %d bytes" % len(html.encode("utf-8")))


if __name__ == "__main__":
    main()
