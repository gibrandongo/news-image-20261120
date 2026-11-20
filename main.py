"""Entry for make.fun news-image-20261120.

Copies the pre-built magazine-cover image entry.png to the output
directory required by the harness. Standard library only, no network,
and fully deterministic: the same input bytes are written every run.
"""

import os
import shutil

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    """Copy entry.png into the harness output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
