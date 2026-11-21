import os

POEM = """The violinist held one note
past where the score said stop.
The hall held its breath with her.
Then silence — not empty,
but full, like a room
after the last chair scraped back
and the song still
deciding whether to end at all."""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(POEM)
