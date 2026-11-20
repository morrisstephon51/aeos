#!/usr/bin/env python3
"""Assert the deployed demo blob still matches its HTML source.

The Supabase edge function serves the Forming Paws demo as a gzipped, base64
"baked" copy of app/forming-paws-live.html. Baking is manual, so the two can
drift silently -- a base64 blob is unreviewable in a diff. This checks them.

Exit 0 = in sync. Exit 1 = drifted (re-bake, or the deploy is stale).
"""
import base64
import gzip
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FUNC = ROOT / "projects/forming-paws/supabase/functions/demo/index.ts"
SRC = ROOT / "projects/forming-paws/app/forming-paws-live.html"


def main() -> int:
    match = re.search(r'const B64 = "([^"]+)"', FUNC.read_text(encoding="utf-8"))
    if not match:
        print(f"FAIL: no B64 literal found in {FUNC.relative_to(ROOT)}")
        return 1

    deployed = gzip.decompress(base64.b64decode(match.group(1))).decode("utf-8")
    source = SRC.read_text(encoding="utf-8")

    if deployed == source:
        print(f"OK: deployed blob matches {SRC.relative_to(ROOT)} ({len(source)} bytes)")
        return 0

    print(f"FAIL: deployed blob has drifted from {SRC.relative_to(ROOT)}")
    print(f"  source   {len(source)} bytes")
    print(f"  deployed {len(deployed)} bytes")
    for tag in ("<!DOCTYPE html>", "<meta charset=", "name=\"viewport\""):
        if tag in deployed and tag not in source:
            print(f"  source is MISSING {tag!r} that the deployed copy has")
        elif tag in source and tag not in deployed:
            print(f"  deployed is MISSING {tag!r} that the source has")
    return 1


if __name__ == "__main__":
    sys.exit(main())
