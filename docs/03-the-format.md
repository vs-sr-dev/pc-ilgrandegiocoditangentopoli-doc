# 03 — The format: two letters, one run-length rule, and a residue that was never there

*Measure: `python tools/px.py --selftest`, 52 checks; `python tools/px.py
--validate iggdt/START.EXE`, which must fail; `python tools/px.py --census
--recurse iggdt --expect 23`, in `notes/px-census.txt`; `python tools/px.py
--palette-report --recurse iggdt`, in `notes/px-palettes.txt`; `python
tools/coverage.py selftest`, 101 checks; `python tools/coverage.py tree --root
iggdt`, in `notes/coverage.txt`.*

---

Eighty-nine and a half per cent of this object is twenty-three files of a format
with **no specification, no vendor and no named producer**. There is nothing to
implement against. Everything below was got by putting a guess to all
twenty-three files at once and printing the places it did not close.

## The grammar

```
+0   2B   'PX'
+2   u16  width          320 on 23 of 23
+4   u16  height         200 on 23 of 23
+6   ...  one run-length stream, to the end of the file

        FF <count> <byte>     a run
        anything else         one literal byte of itself
```

`0xFF` is the commonest byte in every one of the twenty-three files — 3,317 of
17,198 in `RESOURCE.FV1` — which is what a run marker looks like from outside.

The stream decodes, on **23 of 23 files**, to exactly:

```
   10 bytes   preamble       five little-endian words: 247, 0, 0, 320, 200
  768 bytes   VGA palette    256 entries, six bits per channel
64000 bytes   pixels         320 x 200, one index each
-------
64778         and 10 + 768 + 320 x 200 = 64778.   RESIDUE 0
```

```
python tools/px.py --census --recurse iggdt --expect 23

opened                                   : 23 of 23
decoded with residue 0                   : 23 of 23
palette is the canonical EGA 16, in order: 23 of 23
palette is six-bit throughout            : 23 of 23
geometry   : 320x200 x23
residues   : +0 x23
preambles  : 1 distinct
             f7 00 00 00 00 00 40 01 c8 00  x23   as words [247, 0, 0, 320, 200]
```

## The one byte of residue, which was an artefact of the test that found it

The pre-briefing swept header lengths 0 to 24 and scored each by asking whether
the first 768 decoded bytes were all below 64 — a six-bit VGA palette. It picked
**13**, where every file decodes to 64,769 bytes against a target of
768 + 64,000 = 64,768, and it reported **one byte of residue it could not
explain**. It was right to report it and right not to explain it.

**The grammar was not the thing that was wrong. The test was.** The preamble's
first byte is `0xF7` = 247, which is greater than 64, so *any* header length that
leaves the preamble inside the stream fails a "the first 768 bytes are a palette"
test no matter how correct it is. Thirteen is simply the offset at which the
preamble has been swallowed by the header down to its last byte.

And thirteen cannot be a header length anyway, because `FF 05 00` sits at raw
offset 7 — **the sweep was cutting a run-length token in half** and getting away
with it only because the halves happened to decode to nothing.

The arithmetic is exact, and `px.py --selftest` asserts it rather than describing
it:

```
decoding from offset 6 instead of 13 yields 9 more bytes:
    F7                    1
    FF 05 00 -> 5 zeros   5
    40  01  C8            3
                        ---
                          9

64769 + 9 = 64778 = 10 + 768 + 64000
```

**The format closes with residue zero on twenty-three files out of twenty-three,
and the byte that was left over is the first byte of a ten-byte preamble.**

## The palette, and the claim is stronger than "it looks EGA"

The pre-briefing observed that 42, 21 and 63 are the EGA values in six-bit VGA
and that entries 0 and 1 were both black. Read one byte later, the entries are
not merely EGA-flavoured — they are **the canonical IBM EGA sixteen, in
canonical order**:

| | | | | | |
|---:|---|---|---:|---|---|
| 0 | 0,0,0 | black | 8 | 21,21,21 | dark grey |
| 1 | 0,0,42 | blue | 9 | 21,21,63 | light blue |
| 2 | 0,42,0 | green | 10 | 21,63,21 | light green |
| 3 | 0,42,42 | cyan | 11 | 21,63,63 | light cyan |
| 4 | 42,0,0 | red | 12 | 63,21,21 | light red |
| 5 | 42,0,42 | magenta | 13 | 63,21,63 | light magenta |
| 6 | 42,21,0 | brown | 14 | 63,63,21 | yellow |
| 7 | 42,42,42 | light grey | 15 | 63,63,63 | white |

**Sixteen entries, sixteen right, on 23 of 23 files.** `px.py` scores this every
run and `--validate` fails loudly if it ever stops being true. The two entries
that looked like duplicate blacks at offset 0 were black and blue with the
boundary in the wrong place.

**And the two sentences here are different sentences.** The files are 256-colour.
The *low sixteen* are EGA. That is what an artist's tool of that era left behind,
and it is not the same as saying the game is an EGA game — it uses 63 to 81
distinct indices, well above sixteen, and [04](04-the-screens.md) shows the
gradients that need them.

## Three palettes over twenty-three screens

```
python tools/px.py --palette-report --recurse iggdt

641be8e1d158   x19
76b4bdadc8f9   x3     RESOURCE.FV6, FV7, FVC
a935bb67aa28   x1     RESOURCE.FV1
```

The three that share the minority palette are **two of the intro pages and the
sheet of letterheads** — the pages drawn on ruled paper. The one that stands
alone is **the main board**, the outdoor scene with the `TANGENTOMETRO` sign,
which is the only screen that needs a sky.

**One artist, one style, and the two exceptions are the two things that are not
the game.**

## The preamble, which is read but not explained

Identical on all twenty-three files, so nothing can be learned from variation:

```
f7 00 00 00 00 00 40 01 c8 00     =  247, 0, 0, 320, 200
```

The last two words repeat the geometry that the raw header already gave. The
first three do not read themselves. A plausible split is a flag byte `0xF7`
followed by an origin at (0,0), which would make the whole thing *flags, x, y,
w, h* — but a plausible split is not a measurement, twenty-three identical
copies cannot distinguish between readings, and this page says so rather than
picking one.

**`FV` in the extension is not explained either.** The names are a clean
one-based sequence and the letters continue the digits; what `FV` stands for is
not in the bytes.

## Where the boundary between header and stream really is

It is under-determined, and that is worth one paragraph because it is the
honest form of the answer.

`0xC8` at raw offset 12 is not `0xFF`, so it encodes itself whether it is called
a header byte or a literal in the stream. A reader that calls the header 6 bytes
and the preamble 10, and a reader that calls the header 13 bytes and the
preamble 1, produce **the same pixels**. This one uses 6 and 10 because that is
the split under which the arithmetic closes at zero with no special case, and
because a header cannot straddle an RLE token.

## The bucket, which this collection has not met before

`pc-rpgmaker2000-doc/docs/09` set the DECODED test: **a format that can be read
and of which the producer has published no description.**

Every previous DECODED entry in `coverage.py` had a producer who could have
published and did not — Microsoft's ITSF, the EasyRPG project's reading of
ASCII's LCF, Chromium's `.pak`. **This object has no producer at all.** There is
no company, no named tool, and until this session there was no named person
either.

The argument for DECODED anyway, in one line: **the test's second clause is a
statement about the state of the documentation, and its truth condition is that
no description exists.** An absent producer satisfies it — vacuously, but it
satisfies it — and the bucket's purpose is to record where the *warrant* came
from. SPECIFIED means somebody else's document did the work; DECODED means this
pipeline's own reading did. Here it was this pipeline's own reading, over
twenty-three files, checked against itself twenty-three times.

**The counter-argument, stated so it can be argued with:** one could say that
"the producer published nothing" and "there is no producer" are different
propositions and that a bucket which cannot tell them apart needs a fourth
member. That would be defensible. It is not taken here because a fourth bucket
whose only member is one game would carry less information than the sentence in
this paragraph.

```
python tools/coverage.py tree --root iggdt

  decoded        23       412954   89.5163 %  PX 320x200 screen -- no
                                              specification, no vendor, no
                                              named producer; read on this
                                              object
```

## The magic, which is an arithmetic agreement and not two letters

`PX` occurs by chance in a few kilobytes — [08](08-against-the-collection.md)
counts 20,109 occurrences of it in one cover disc. The signature added to
`coverage.py` is therefore not `b"PX"`. It decodes ten bytes of the stream and
requires that **the geometry stated in the preamble equal the geometry stated in
the header**. Three of the six new selftest checks are refusals, and the first
of them is a file that begins `PX` and is not one.

```
a PX whose stream repeats its own geometry is DECODED       ok
a file that merely BEGINS `PX` is REFUSED                   ok
a PX whose preamble geometry DISAGREES is REFUSED           ok
a PX with a zero dimension is REFUSED                       ok
a PX too short to decode ten bytes is REFUSED               ok
PX is tested before every text codec                        ok
```

## The negative control, run before the census

```
python tools/px.py --validate iggdt/START.EXE

FAIL  START.EXE: not a PX file: first two bytes are 4d 5a, wanted b'PX'
FATAL: 1 of 1 files failed                                      exit 1

python tools/px.py --validate iggdt

px: iggdt is a directory; this reader wants one file.           exit 1
```

`--recurse` selects on the magic and never on a name, because the twenty-three
screens, one DOS executable and one high-score table are in the same flat folder
and an extension filter is the defect `mzcensus.py` has been carrying for
fourteen objects.
