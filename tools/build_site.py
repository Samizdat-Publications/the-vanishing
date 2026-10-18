"""Assemble site-dist/ for Cloudflare Pages from the built dashboard.

    python3 tools/merge.py && python3 tools/build_dashboard.py
    python3 tools/build_site.py
    npx --yes wrangler@4 pages deploy site-dist --project-name the-vanishing --branch main

The page becomes index.html; the fifteen published photographs go alongside it. The
uncropped originals in assets/photos/_source are working files and are not published.
"""

import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTO_EXT = (".jpg", ".jpeg", ".png", ".webp")


def main():
    page = os.path.join(ROOT, "dist", "the-vanishing.html")
    if not os.path.isfile(page):
        raise SystemExit("dist/the-vanishing.html is missing; run tools/build_dashboard.py first")

    out = os.path.join(ROOT, "site-dist")
    photos_out = os.path.join(out, "assets", "photos")
    os.makedirs(photos_out, exist_ok=True)
    for name in os.listdir(photos_out):
        os.remove(os.path.join(photos_out, name))

    shutil.copyfile(page, os.path.join(out, "index.html"))
    photos_src = os.path.join(ROOT, "assets", "photos")
    n = 0
    for name in sorted(os.listdir(photos_src)):
        if name.lower().endswith(PHOTO_EXT):
            shutil.copyfile(os.path.join(photos_src, name), os.path.join(photos_out, name))
            n += 1

    with open(os.path.join(out, "_headers"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("/assets/*\n  Cache-Control: public, max-age=604800\n")

    print("site-dist/index.html plus %d photographs" % n)


if __name__ == "__main__":
    main()
