# Quarto fills listing thumbnails after rendering without loading="lazy",
# so every news photo downloads up front. Add the attribute here.
import os
import re

out_dir = os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site")
files = os.environ.get("QUARTO_PROJECT_OUTPUT_FILES", "").split("\n")

for path in filter(None, files):
    if not path.endswith(".html") or not os.path.exists(path):
        continue
    with open(path, encoding="utf-8") as f:
        html = f.read()
    updated = re.sub(r'<img (?![^>]*\bloading=)([^>]*class="thumbnail-image)', r'<img loading="lazy" \1', html)
    if updated != html:
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
