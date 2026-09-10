# 01 — The object: twenty-six files, one minute, and the lowest opening figure this collection has recorded

*Measure: `python tools/treecensus.py iggdt` and `python tools/hashall.py iggdt`,
in `notes/treecensus.txt` and `notes/hashall.txt`; `python tools/mtimes.py iggdt
--waves`, in `notes/mtimes.txt`; `python tools/coverage.py tree --root iggdt`,
in `notes/coverage.txt`; `python tools/entropy.py iggdt`, in
`notes/entropy.txt`.*

---

**Il grande gioco di Tangentopoli** is an MS-DOS game in Italian about the Milan
bribery investigations. It is twenty-six files in one flat folder, it installs
itself into `C:\TANGENT`, and it names no publisher, no author, no copyright
holder and no year.

That last sentence was true when this session started. It is no longer true, and
[05](05-the-names.md) is why: the object names four people and gives itself a
date, and it does both in places no string search reaches.

## The census

```
python tools/treecensus.py iggdt

files           : 26
directories     : 0        one flat folder
bytes           : 461317

python tools/hashall.py iggdt
files 26   bytes 461317   distinct sha1 26   unreadable 0
```

**Twenty-six files and twenty-six distinct hashes.** Nothing in this object is a
copy of anything else in it.

| file | bytes | | file | bytes |
|---|---:|---|---|---:|
| `HIGHSCOR.TNG` | 104 | | `RESOURCE.FVD` | 13,073 |
| `INSTALL.BAT` | 4,814 | | `RESOURCE.FVE` | 12,844 |
| `RESOURCE.FV1` | 17,198 | | `RESOURCE.FVF` | 5,620 |
| `RESOURCE.FV2` | 29,245 | | `RESOURCE.FVG` | 30,019 |
| `RESOURCE.FV3` | 26,114 | | `RESOURCE.FVH` | 38,976 |
| `RESOURCE.FV4` | 42,828 | | `RESOURCE.FVI` | 10,626 |
| `RESOURCE.FV5` | 43,428 | | `RESOURCE.FVJ` | 15,872 |
| `RESOURCE.FV6` | 9,440 | | `RESOURCE.FVK` | 7,080 |
| `RESOURCE.FV7` | 11,415 | | `RESOURCE.FVL` | 19,414 |
| `RESOURCE.FV8` | 9,583 | | `RESOURCE.FVM` | 17,291 |
| `RESOURCE.FV9` | 9,508 | | `RESOURCE.FVN` | 19,048 |
| `RESOURCE.FVA` | 9,342 | | `START.EXE` | 43,445 |
| `RESOURCE.FVB` | 6,772 | | | |
| `RESOURCE.FVC` | 8,218 | | | |

The resource names run `FV1`..`FV9` then `FVA`..`FVN`: a one-based sequence of
**twenty-three**, base ten continued into letters, with no gap. It is not the
order the player meets them in, and [04](04-the-screens.md) shows why — the
title screen is number four.

## The four families, and the denominator each of them names

```
python tools/coverage.py tree --root iggdt
```

| family | files | bytes | share of 461,317 |
|---|---:|---:|---:|
| `RESOURCE.FV1..FVN`, magic `PX` | 23 | 412,954 | **89.5163 %** |
| `START.EXE`, a DOS MZ | 1 | 43,445 | 9.4176 % |
| `INSTALL.BAT`, cp437 text | 1 | 4,814 | 1.0435 % |
| `HIGHSCOR.TNG`, no magic at all | 1 | 104 | 0.0225 % |
| **sum** | **26** | **461,317** | **100.0000 %**, residue 0 |

**The 89.5163 % is a re-derivation and it corrects an inherited figure.** The
pre-briefing carries 413,058 bytes and 89.5389 % for the twenty-three
resources; that is the twenty-three resources **plus `HIGHSCOR.TNG`**, and its
own four-row split therefore sums to 461,421 against an object of 461,317 —
over by 104, which is `HIGHSCOR.TNG` exactly.
[09](09-the-box-and-the-corrections.md) C.1.

## One mtime, and it is Christmas Eve

```
python tools/mtimes.py iggdt --waves

wave 1   1996-12-24 23:32:00 .. 1996-12-24 23:32:00
         26 files   461317 bytes   100.00%
```

**One wave, to the second, over all twenty-six files.** That is the clean case
of the rule `pc-rpgmakermv-doc/docs/08` wrote — *an installation that has never
been patched carries one wave, because every file's mtime is the moment of the
single operation that wrote it.*

What the wave does **not** carry is the game's date, and
[07](07-the-clocks.md) is a whole chapter about that, because Tangentopoli began
in 1992 and the object turns out to state a year of its own.

## The coverage, which opened lower than anything here and closed higher

```
                    files      bytes       share
OPENING
  specified             2      48,259    10.4611 %
  opaque               24     413,058    89.5389 %

CLOSING
  specified             2      48,259    10.4611 %   MZ, and cp437 text
  decoded              23     412,954    89.5163 %   PX -- read on this object
  opaque                1         104     0.0225 %   HIGHSCOR.TNG
  SUM                  26     461,317   100.0000 %   residue 0
```

**10.4611 % is the lowest figure any object in this collection has started at.**
`pc-popcorn-doc` is recorded in the index at 13.0927 %, but that is a *closing*
figure and this was an *opening* one, so the two are not comparable and the only
sentence worth writing is the narrow one.

**It closes at 99.9775 % identified, and the whole 89.5163 points of that come
from twenty-three files of a format with no specification, no vendor and no
named producer.** The bucket is DECODED and the argument for it is
[03](03-the-format.md).

**And the one file left in OPAQUE is the one file that is read completely.**
`HIGHSCOR.TNG` has no magic number — it has no signature bytes of any kind —
and `coverage.py` classifies by magic, so a magic-based classifier cannot
identify it however well it is understood. [05](05-the-names.md) reads all 104
bytes and names all four records. **Identification and reading are two different
questions and this object separates them by 104 bytes.**

## Entropy, which says which file is packed

```
python tools/entropy.py iggdt

START.EXE                       7.8145      1 block above 7.5
every RESOURCE.FV*    3.8470 .. 5.0790      0 blocks above 7.5
```

The resources are run-length coded and read like it. `START.EXE` does not, and
[06](06-the-program.md) is about the 43,445 bytes that ask for 318,704 more.

## What is not in this object

Written once, with the numbers, because saying it six times would be worse:

**no publisher, no author string, no copyright, no version resource, no COFF
timestamp, no readme, no e-mail address, no build path, no UUID, no third-party
component, and no byte in common with any of 108 other repositories.**

That is not six failures. It is the shape of a program written by a few people
in Italy and put on a floppy disk, and [08](08-against-the-collection.md) counts
it once and moves on.

**The only thing the program says about itself in plain bytes is fifty-two
characters in the padding of its own DOS header:**

```
TANGENTOPOLI - V. 1.0 - (Perche' guardi qua dentro?)
```

*Why are you looking in here?* — addressed, twenty-nine years later, to exactly
the person doing this. [06](06-the-program.md) answers it.
