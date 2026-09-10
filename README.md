# Il grande gioco di Tangentopoli — a measured description

An MS-DOS game in Italian about the Milan bribery investigations, in twenty-six
files, with no publisher, no copyright string, no readme and no date that is not
a file system's. Eighty-nine and a half per cent of it is an undocumented format
that turns out to hold everything the game says — including the names of the
four people who made it.

Nothing here was executed, installed or emulated. Every figure on every page
carries the command that produces it again — with one marked exception, a
section of [04](docs/04-the-screens.md) that records the recollection of
somebody who played this game as a child, kept separate from every count in the
repository because it is testimony and not a measurement.

| | |
|---|---|
| title | *Il grande gioco di Tangentopoli*, `V. 1.0` |
| platform | MS-DOS, VGA mode 13h, 320 × 200 × 256 |
| files / bytes | 26 / 461,317, one flat folder, 26 distinct sha1 |
| mtime | 1996-12-24 23:32:00, one wave, 26 of 26 |
| **made by** | **Guglielmo Duccoli, Roberto Piazzolla, Michele Ferrara, Thimoty Barbieri** |
| identified | **10.4611 % opening → 99.9775 % closing** |
| the format | `PX`, `FF <count> <byte>`, 10 + 768 + 64,000 = 64,778, **residue 0 on 23 of 23** |
| the executable | 43,445 bytes demanding 318,704 more, **0 of 30 packer signatures**, 526 bytes of stub disassembled at 100 % |
| the high-score table | 104 bytes, key `x ^ 0xFE`, four names, four zero scores |
| against the collection | **0 crossings of 26**, over 108 repositories |
| tools | 572 Python files, 4 written here, **273 selftest checks, 0 failures** |

**10.4611 % is the lowest figure any object in this collection has started at.**
It closed at 99.9775 % because twenty-three files of a format with no
specification, no vendor and no named producer turned out to close to the byte.

**The names are the finding.** Neither place that holds them is a string: one is
painted in the pixels of a 320 × 200 credits screen, the other is a hundred and
four bytes XORed with `0xFE`. Every name-finding tool in the box returned zero,
correctly, and went on returning zero until 89.5163 % of the object stopped
being opaque.

| | chapter |
|---|---|
| 01 | [The object](docs/01-the-object.md) — twenty-six files, one minute, and the lowest opening figure this collection has recorded |
| 02 | [The technical sheet](docs/02-the-technical-sheet.md) — every figure with the command that makes it again |
| 03 | [The format](docs/03-the-format.md) — two letters, one run-length rule, and a residue that was never there |
| 04 | [The screens](docs/04-the-screens.md) — a thermometer for bribes, and a game that says everything it has to say in pixels |
| 05 | [The names](docs/05-the-names.md) — four people, written twice, and neither time as text |
| 06 | [The program](docs/06-the-program.md) — forty-three kilobytes nobody signs, and a decision about how far to go in |
| 07 | [The clocks](docs/07-the-clocks.md) — a file system, a sentence in a picture, and a list of DOS versions |
| 08 | [Against the collection](docs/08-against-the-collection.md) — zero of twenty-six, and the same two letters twice |
| 09 | [The box and the corrections](docs/09-the-box-and-the-corrections.md) — four tools, 273 checks, eleven things that were wrong, and one of them was mine |

**Nine chapters, and the reason is twenty-six files.** The last ten objects
documented here ran to sixteen, eighteen and nineteen; an object of 461,317
bytes with four families of file in it does not have sixteen chapters' worth of
distinct subject, and padding it out would have cost the space that
[04](docs/04-the-screens.md) and [05](docs/05-the-names.md) needed.

## What is in this repository

`docs/` the nine chapters. `notes/` twenty-four files of captured tool output,
one per measurement. `tools/` 572 Python files, of which `px.py`, `tngscore.py`,
`dosdis.py` and `dospack.py` were written here and `coverage.py` was modified.

**The game is not here.** Neither are the twenty-three PNG — the command that
writes them is on [04](docs/04-the-screens.md) and takes about a second.

## The sentence the program says about itself

Fifty-two characters, measured to fit fifty-two bytes of DOS header padding,
where only somebody with a hex editor would ever see them:

> `TANGENTOPOLI - V. 1.0 - (Perche' guardi qua dentro?)`

*Why are you looking in here?* — Because the answer was not in there. It was in
the pictures.
