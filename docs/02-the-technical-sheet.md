# 02 — The technical sheet: every figure on this page has the command that makes it again

*Measure: this page is the index of measurements. Every row carries the command
that produces it and the file in `notes/` that holds the output.*

---

## The object

| | | command |
|---|---|---|
| title | *Il grande gioco di Tangentopoli* | drawn in `RESOURCE.FV4`; printed by `INSTALL.BAT` |
| platform | MS-DOS, VGA mode 13h, 320 × 200 × 256 | `python tools/px.py --census --recurse iggdt` |
| language | Italian throughout | — |
| version | `V. 1.0` | `python tools/dospack.py iggdt/START.EXE` |
| files | 26 | `python tools/treecensus.py iggdt` |
| bytes | 461,317 | `python tools/treecensus.py iggdt` |
| directories | 0 | `python tools/treecensus.py iggdt` |
| distinct sha1 | 26 of 26 | `python tools/hashall.py iggdt` |
| mtime | 1996-12-24 23:32:00, one wave, 26 of 26 | `python tools/mtimes.py iggdt --waves` |
| installs to | `%1\TANGENT`, `%1` in C: .. P: | `INSTALL.BAT` |
| identified | **99.9775 %** | `python tools/coverage.py tree --root iggdt` |

## The people, and where each name is written

| name | credited as | `RESOURCE.FV3` | `HIGHSCOR.TNG` |
|---|---|---|---|
| Guglielmo Duccoli | *ideato da* | yes | `GUGLIELMO` |
| Roberto Piazzolla | *programmazione* | yes | `ROBERTO` |
| Michele Ferrara | *grafica* | yes | `MICHELE` |
| Thimoty Barbieri | *musiche e suoni* | yes | `TIMOTHY` |

```
python tools/px.py --render iggdt/RESOURCE.FV3 --out _work/png \
    --crop 20,125,280,60 --zoom 3
python tools/tngscore.py iggdt/HIGHSCOR.TNG \
    --credits GUGLIELMO,ROBERTO,MICHELE,THIMOTY        (notes/tngscore.txt)
```

**Neither name is a string.** One set is drawn in pixels; the other is stored
`x ^ 0xFE`. [05](05-the-names.md).

## The `PX` format

| | | command |
|---|---|---|
| magic | `PX` at offset 0, on 23 of 26 files | `python tools/sigcount.py iggdt --hex 5058` |
| header | `'PX'`, u16 width, u16 height — 6 bytes | `python tools/px.py --census --recurse iggdt` |
| stream | one RLE from offset 6 to end of file | as above |
| rule | `FF <count> <byte>`; anything else is a literal | as above |
| decodes to | 10 + 768 + 64,000 = **64,778 bytes** | as above |
| residue | **0 on 23 of 23** | as above |
| geometry | 320 × 200 on 23 of 23 | as above |
| palette | 256 entries, 6-bit VGA; low 16 are canonical EGA in order on **23 of 23** | `python tools/px.py --palette-report --recurse iggdt` |
| distinct palettes | **3** — 19, 3, 1 | as above |
| preamble | 1 distinct over 23: words `247, 0, 0, 320, 200` | as above |
| indices actually used | 3 to 81 of 256 | as above |

## `START.EXE`

| field | value | |
|---|---:|---|
| `e_magic` | `0x5A4D` | `python tools/dospack.py iggdt/START.EXE --sweep --relocator` |
| `e_cblp` / `e_cp` | 437 / 85 | 43,445 mod 512 = 437; they agree |
| `e_crlc` | 1 | one relocation, at `0x0007` |
| `e_cparhdr` | 6 | header 96 bytes |
| `e_minalloc` | 19,919 paragraphs | **318,704 bytes demanded** |
| `e_ss:e_sp` | `0x0A9C:0x0200` | |
| `e_cs:e_ip` | `0xFFF0:0x0100` | the PSP minus 16 paragraphs = the first image byte |
| `e_lfarlc` | `0x0052` | |
| slack after image | 0 | |
| reserved area `0x1C..0x51` | 54 bytes | `0C 01` then 52 characters of message |
| entropy of the image | 7.8152 bits/byte | |
| distinct byte values | 256 of 256 | |
| packer signatures | **0 of 30 countable, anywhere and in place** | |
| entry stub | 51 bytes, 25 instructions | `python tools/dosdis.py iggdt/START.EXE --at 96 --length 51 --org 0x100` |
| relocated stub | **file offsets 164..751, 588 bytes** | computed, not read off |
| — of which code | 526 bytes, 290 instructions, decoded 100 % | `python tools/dosdis.py iggdt/START.EXE --at 164 --length 526 --org 0` |
| — of which tables | 62 bytes at `020E`, indexed from four sites | |
| branch targets landing on an instruction boundary | **54 of 54** | `--targets` |

## `HIGHSCOR.TNG`

| | | |
|---|---|---|
| bytes | 104 = 4 records of 26 = 6 + 20 | `python tools/tngscore.py iggdt/HIGHSCOR.TNG` |
| keys tried | 512 — 256 of `x ^ k`, 256 of `k - x` | |
| survive structure | 6 | |
| survive a zero score | 2 | |
| survive corroboration | **1: `x ^ 0xFE`** | |
| score field | six zero bytes, 4 of 4 records | |
| filler | `$`, the DOS `INT 21h AH=09` terminator | |
| names | `ROBERTO` `GUGLIELMO` `TIMOTHY` `MICHELE` | |

## `INSTALL.BAT`

| | |
|---|---|
| bytes | 4,814, CRLF, cp437 |
| bytes ≥ 0x80 | 302 in the file, **0 in the first 512** |
| box-drawing | 252 × `0xCD`, 38 × `0xBA`, 2 each of `0xC9 0xBB 0xC8 0xBC` |
| copies | `*.exe`, `resource.*`, and `leggimi.doc` *if it exists* |
| does not copy | `HIGHSCOR.TNG` |
| `LEGGIMI.DOC` | **absent from this folder** |

`coverage.py` files it as **plain text, ASCII**. It is cp437 and the classifier
is not malfunctioning: `_printable` reads the first 512 bytes and every one of
this file's 302 high bytes is in the banner at the end.
[09](09-the-box-and-the-corrections.md) C.10 explains why that was left alone.

## Against the collection

| | | command |
|---|---|---|
| repositories swept | 108 | `python tools/crossall.py _work/sha1-all.txt --collection .. --skip pc-ilgrandegiocoditangentopoli-doc` |
| crossings | **0 of 26** | as above |
| files in CLIC 02/97 beginning `PX` | **0 of 3,343** | `python tools/sigcount.py ../pc-clic0297-doc --hex 5058` |
| occurrences of `PX` anywhere in it | 20,109, in 498 files | as above |
| files in this object beginning `PX` | **23 of 26** | `python tools/sigcount.py iggdt --hex 5058` |
| the four surnames elsewhere in 137 repositories | 0 | [08](08-against-the-collection.md) |

## The box

| | | command |
|---|---|---|
| Python files | 572 | `ls -1 tools/*.py \| wc -l` |
| written this session | 4 — `px`, `tngscore`, `dosdis`, `dospack` | `python tools/toolsdiff.py ../pc-rpgmakermv-doc/tools --expect-differing 1` |
| modified this session | 1 — `coverage.py` | as above |
| selftest checks | **273, 0 failures**, `PYTHONIOENCODING` absent | `notes/selftests.txt` |
| `dirguard --survey` | 216 raised of 571 | `python tools/dirguard.py --survey --tools tools` |
| `nameguard --survey` | 7 of the 10 that emit a name | `python tools/nameguard.py --survey --tools tools` |
| `refusals.py` | 60 of 92; `argparse` **23 for the tenth time** | `python tools/refusalclass.py notes/refusals.txt` |
| rule-0 hook | see `notes/rule0.txt` | `python tools/rule0hook.py --report` |
