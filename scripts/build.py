#!/usr/bin/env python3
"""Build a self-contained index.html using the checked-in source and libraries."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
LIBRARIES = {
    "https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js": "pdf-lib-1.17.1.min.js",
    "https://cdn.jsdelivr.net/npm/@pdf-lib/fontkit@1.1.1/dist/fontkit.umd.min.js": "fontkit-1.1.1.umd.min.js",
    "https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js": "jszip-3.10.1.min.js",
    "https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js": "papaparse-5.4.1.min.js",
}

def build():
    html = (ROOT / "src/app.html").read_text()
    for url, filename in LIBRARIES.items():
        library = (ROOT / "vendor" / filename).read_text()
        # Prevent a string in a library from ending its enclosing HTML script.
        library = re.sub(r"</script", r"<\/script", library, flags=re.I)
        # Source maps are development aids, not runtime dependencies.
        library = re.sub(r"(?m)^//# sourceMappingURL=.*$", "", library)
        tag = '<script src="' + url + '"></script>'
        if html.count(tag) != 1:
            raise ValueError("Expected one script tag for " + filename)
        html = html.replace(tag, "<script>\n" + library + "\n</script>")
    (ROOT / "index.html").write_text(html)
    print("Built index.html:", (ROOT / "index.html").stat().st_size, "bytes")

if __name__ == "__main__":
    build()
