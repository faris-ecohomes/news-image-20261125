# news-image-20261125 entry (Python 3.13, standard library only).
# The poster is drawn in advance and shipped as entry.png beside this file;
# the program only copies it to $MAKEFUN_OUTPUT_DIR/entry.png, after checking
# that it is a whole 1024x1024 PNG. No network, no rendering, no randomness:
# both runs write byte-identical output.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import struct
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")

    with open(src, "rb") as f:
        head = f.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        sys.exit("entry.png is not a PNG")
    width, height = struct.unpack(">II", head[16:24])
    if (width, height) != (1024, 1024):
        sys.exit("entry.png is not 1024x1024")
    if os.path.getsize(src) > 1048576:
        sys.exit("entry.png is over 1 MiB")

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
