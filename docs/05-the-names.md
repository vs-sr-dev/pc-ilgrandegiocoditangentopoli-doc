# 05 — The names: four people, written twice, and neither time as text

*Measure: `python tools/px.py --render iggdt/RESOURCE.FV3 --out _work/png --crop
20,125,280,60 --zoom 3`; `python tools/tngscore.py --selftest`, 20 checks;
`python tools/tngscore.py iggdt/HIGHSCOR.TNG` with no `--credits`, which must
refuse; `python tools/tngscore.py iggdt/HIGHSCOR.TNG --credits
GUGLIELMO,ROBERTO,MICHELE,THIMOTY`, in `notes/tngscore.txt`.*

---

The pre-briefing's list of what this object does not have runs: *no publisher
named, no author named, no copyright string, no version resource, no COFF
timestamp, no readme.* Every line of it was arrived at honestly, by looking for
strings, and every tool in this box that reads a name came back with nothing.

**The object names four people. It does it twice. Neither time in a string.**

## The first place: paint

`RESOURCE.FV3` is a 320 × 200 screen. Its bottom half is a red-bordered panel,
and magnified three times the panel reads:

```
python tools/px.py --render iggdt/RESOURCE.FV3 --out _work/png \
    --crop 20,125,280,60 --zoom 3
```

> ideato da **Guglielmo Duccoli**
> programmazione: **Roberto Piazzolla**
> grafica: **Michele Ferrara**
> musiche e suoni: **Thimoty Barbieri**

*Devised by Guglielmo Duccoli / programming: Roberto Piazzolla / graphics:
Michele Ferrara / music and sound: Thimoty Barbieri.*

Four roles, four people, on the same screen as a `VUOI TORNARE AL DOS? S/N`
prompt. **No company appears anywhere on it.**

**A credits screen is not an unusual place to put credits.** What is unusual is
that this one was invisible to a pipeline that had already run `sift.py`,
`namescan.py`, `uuidscan.py`, `vendorhash.py`, `verres.py` and `stampcheck.py`
over the object and got zero from all six — correctly, because there is no
string here to find. The names became visible the moment 89.5163 % of the object
stopped being opaque, and not one moment earlier.

## The second place: a hundred and four bytes and one wrong bit

`HIGHSCOR.TNG` is 104 bytes = 4 records × 26 = 6 bytes of score + 20 of name.
Every record opens with six `0xFE`; the filler is `0xDA`.

The pre-briefing's reading was the one-byte complement, and it argued for it
carefully: `~0xDA` is `0x25` = `%`, `~0xFE` is `0x01`, and the affine family
`k - x` has exactly one member that fits both fields. It read out

```
SNCDSUN     FTFMHDMLN     UHLNUIX     LHBIDMD
```

and said — correctly — that those are not Italian names and that the reading
stopped there. **Stopping there was the right call. The reading was one bit
away.**

The key is `x ^ 0xFE`, which differs from `x ^ 0xFF` in the low bit alone. So
every letter above is the right letter with its bottom bit flipped: `S`/`R`,
`N`/`O`, `C`/`B`, `U`/`T`. The sweep that would have found it — all 256 keys of
`x ^ k` — was never run; the probe tried the affine family and the single mask
`x ^ 0x80`.

## Three stages, and the third one comes from outside the file

`tngscore.py` will not pick a key by looking at the output, because looking at
the output is how you get the answer you wanted. It narrows in declared steps.

**Stage 1 — structure. 512 → 6.** Every key of `x ^ k` and `k - x`, kept only
if each record's 20-byte name field is a run of A–Z followed by a run of one
single non-letter filler. Nothing in that test names `0xFE` or `$`.

```
xor 0xFE   xor 0xFF   sub 0x00   sub 0x01   sub 0xFE   sub 0xFF
```

**Stage 2 — the score. 6 → 2.** A default table that has never been played on
has no scores in it, so the six-byte score field must be six zero bytes. Two
keys survive, and they agree on something neither was asked about: **both make
the filler `$`**, which is the terminator `INT 21h AH=09` stops printing at and
exactly what a 1990s DOS program pads a printable field with. The same `$`
closes `START.EXE`'s own error string, `Manca memoria    $`.

**Stage 3 — corroboration, and the corroborating artefact is a picture.**

```
xor  0xFE   ROBERTO     GUGLIELMO   TIMOTHY   MICHELE
sub  0xFE   RMBCRTM     ESELGCLKM   TGKMTHW   KGAHCLC
```

Choosing between those by eye would be fitting. `--credits` instead counts exact
matches against the names the object states **somewhere else entirely** — in the
pixels of `RESOURCE.FV3`, recovered by a different tool from a different file
under a different format:

```
xor  0xFE   3 of 4 exact   not matched: TIMOTHY
sub  0xFE   0 of 4 exact
```

Run without `--credits` the tool exits 2 and says so:

> STAGE 3 corroboration : NOT RUN. 2 keys still stand and this tool will not
> pick between them by eye.

## The four records

```
rec  score                name         field
1    00 00 00 00 00 00    ROBERTO      7 letters + 13 x '$'
2    00 00 00 00 00 00    GUGLIELMO    9 letters + 11 x '$'
3    00 00 00 00 00 00    TIMOTHY      7 letters + 13 x '$'
4    00 00 00 00 00 00    MICHELE      7 letters + 13 x '$'
```

**The shipped high-score table is the four authors' first names with a score of
zero each.** Nobody had played it. It is the same four people as the credits
screen, given as forenames where the credits give both names, which is why the
lengths line up: 7, 9, 7, 7 against Roberto, Guglielmo, Timothy, Michele.

## The one that does not match, and it is left as a mismatch

Stage 3 scores **3 of 4**, not 4 of 4. The credits screen paints **`Thimoty`**;
the high-score table stores **`TIMOTHY`**.

That is not an error to be resolved. It is one person spelled two ways in the
only two places this object says who made it — the Italian spelling in the art
and the English one in the data, written by two different people on two
different days. The tool reports it as a miss and names it rather than
normalising it away, because a corroboration that quietly accepts near-matches
is not a corroboration.

## What this does not settle

**Not the publisher.** Four people are named and no company is. `INSTALL.BAT`
looks for a `LEGGIMI.DOC` that is not in this folder, and a readme is where a
game of this kind names its distributor.

**Not the six zero bytes.** Six is the width of a Turbo Pascal `Real` and zero
is its zero, which would be a neat fit for a 1996 Italian DOS game — and nothing
in 104 bytes tells a `Real` from six zeroed bytes of anything else.
`tngscore.py` prints *six zero bytes* for that reason.

**And not the judge's name.** The player character is `Giudice De Petris`
([04](04-the-screens.md)). The best-known magistrate of the Milan investigations
was Antonio Di Pietro. The resemblance is there and this page will not do more
with it than put the two names next to each other.

## Why this is the answer to the question in the header

`START.EXE` carries, in fifty-two bytes of header padding, *(Perche' guardi qua
dentro?)* — **why are you looking in here?**

Because the answer was not in there. It was in the pictures and in a hundred and
four bytes, and the joke's author signed the game in three separate places —
the padding, the credits screen, the default score table — **none of which is a
string a program could have found.** The one that answers the question is the
one that was hardest to look at.
