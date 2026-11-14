# Food-picture entry: copies the picture beside this file to /output/entry.png.
# A plain byte copy, so both runs of the program write identical bytes.
# (entry.png holds JPEG bytes; the competition tells PNG from JPEG by the
# first bytes, so the name stays entry.png either way.)
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(
        os.path.join(here, "entry.png"),
        os.path.join(out, "entry.png"),
    )


if __name__ == "__main__":
    main()
