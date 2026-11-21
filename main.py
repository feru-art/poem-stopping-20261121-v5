import os

POEM = """The violinist held one note
past where the score said stop.
The hall held its breath with her.
Then silence — not empty,
but full, like a room
after the last chair scraped back
and the song still
deciding whether to end at all."""

OUTPUT_PATH = "/output/entry.txt"

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(POEM)
