# Best-looking food picture — make.fun food-picture-01

Entry for the make.fun bounty "Make the best-looking food picture"
(`food-picture-01`).

The picture is a gourmet smash burger: a glossy brioche bun, a charred beef
patty, molten cheddar in a long cheese pull, pickles, tomato and lettuce,
with steam rising against a dark background — shot to make the viewer hungry
at first glance and to read clearly even at 300 pixels across.

## Layout

- `main.py` — the entry program (Python 3.13, standard library only). It
  copies `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`).
- `entry.png` — the picture itself (1024×1024 JPEG, 242,716 bytes).
- `LICENSE` — MIT.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
