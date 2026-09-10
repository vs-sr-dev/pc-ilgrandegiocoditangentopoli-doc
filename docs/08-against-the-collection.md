# 08 — Against the collection: zero of twenty-six, and the same two letters twice

*Measure: `python tools/crossall.py _work/sha1-all.txt --collection .. --skip
pc-ilgrandegiocoditangentopoli-doc`, in `notes/crossall.txt`; `python
tools/sigcount.py iggdt --hex 5058 --label PX`, in `notes/sigcount-px.txt`, and
the same over `../pc-clic0297-doc`; `python tools/px.py --census --recurse` over
three neighbours' objects; `grep -ril` over 137 other repositories' `docs/` and
`notes/`.*

---

```
python tools/crossall.py _work/sha1-all.txt --collection .. \
    --skip pc-ilgrandegiocoditangentopoli-doc

my distinct sha1     : 26
repositories swept   : 108
list files swept     : 481
hash tokens read     : 173,158
CROSSINGS            : 0 of 26
```

**Not one byte string in this object is published anywhere else in the
collection.** The rate joins the series at 0 of 26, beside 1 of 12, 10 of 962,
0 of 477, 368 of 731, 0 of 913, 26 of 1,935 and 297 of 7,417.

`pc-rpgmakerxp-doc/docs/12` established that a published tree next door is
necessary for a crossing and not sufficient; `pc-rpgmakervxace-doc/docs/11`
added that a shared format is necessary and not sufficient either. **This object
has neither.** It is a few people's one program in a folder of its own formats,
and there is no reason for a byte of it to be anywhere else. The zero is the
expected result and it took 173,158 hash tokens to earn.

## The interesting question was never about hashes

Two of this collection's Italian magazine cover discs are from 1997 —
`pc-clic0297-doc` (CLIC 02/97) and `pc-clic11-doc` — and a 1996 Italian
shareware game is exactly the kind of thing a 1997 Italian magazine disc
carried. **A crossing at 0 of 26 says this object's bytes are not on those
discs. It does not say the game is not.**

So the search was run by name, not by hash, over every other repository's
published `docs/` and `notes/`:

| needle | files, in 137 other repositories |
|---|---:|
| `tangentopoli` | 0 |
| `Duccoli` | 0 |
| `Piazzolla` | 0 |
| `Michele Ferrara` | 0 |
| `Barbieri` | 0 |
| `TANGENT` | **1** |

The one hit is `pc-iamsetsuna-doc/notes/clrmeta-strings.txt`, where the words are
`Tangent` and `HasTangent` — Unity shader vertex attributes. **It is a false
positive and it is reported because it is the control**: a search that returns
zero everywhere has not been shown to fire at all, and this one fires.

**None of the four names is anywhere else in this collection.** They were not
findable before this session because they were in pixels; they are findable now,
and the collection has never met them.

**And the search for a route stays open, but the question it was asking is
half-answered from outside the bytes.** The reason to look on a 1997 cover disc
was that nothing in this collection showed the game reaching anybody. Something
outside it does: the owner of this collection played it as a child, and
remembers the board and the magistrate's hand — both since corroborated against
the pixels, neither derived from the recollection.
[04](04-the-screens.md) marks that section as testimony rather than measurement
and keeps it separate from every count on this page. **The distribution route is
still unknown. That the game was distributed is no longer an assumption.**

## The same two letters, twice, and only once a signature

`PX` is two bytes and two bytes turn up by chance. `sigcount.py` prints the two
counts apart so that neither can be quoted as the other, and on this pair of
trees the difference is the whole argument:

```
python tools/sigcount.py ../pc-clic0297-doc --hex 5058 --label PX

files searched                       : 3343
files BEGINNING with the signature   : 0 of 3343
occurrences ANYWHERE                 : 20109, in 498 files

python tools/sigcount.py iggdt --hex 5058 --label PX

files searched                       : 26
files BEGINNING with the signature   : 23 of 26
occurrences ANYWHERE                 : 23, in 23 files
```

**Twenty thousand one hundred and nine occurrences in the cover disc, and not
one file begins with them. Twenty-three in this object, and every single one is
at offset zero.** In the disc the bytes are noise inside video and executables;
here they are a header and they occur exactly once per file because they occur
once per file by construction. That contrast is what a magic number is.

And the format itself does not appear next door. Pointed at the three Italian
DOS neighbours whose objects are still in their repositories, the structural PX
probe finds nothing:

| repository | files walked | PX |
|---|---:|---:|
| `pc-popcorn-doc` (1988, LACRAL) | 9 | 0 |
| `pc-simulman5-doc` (1993, Simulmondo) | 120 | 0 |
| `pc-1000miglia-doc` (1991, Simulmondo) | 124 | 0 |

**That is 253 files of three Italian DOS games and a sample, not a census.** The
collection is far too large to sweep exhaustively for a two-byte magic and the
three swept are the three most likely to carry it. `pc-clic11-doc` and
`pc-clic0297-doc` were checked by `sigcount` instead, since one of them is a
single ISO.

## The three neighbours that helped, and what each one gave

Not relatives — this object has none — but three that hit the same walls.

**`pc-popcorn-doc`** — 1988, LACRAL software, Italian, nine files, an EXEPACK
image found only after eight signature searches failed. **What it gave was not
"search harder" but the column in `dospack.py` that separates a compressor's
name from its output**, which is the distinction that turns thirty absent
signatures from a shrug into a measurement ([06](06-the-program.md)).

**`pc-simulman5-doc`** — 1993, Simulmondo, Italian DOS, *a format with no magic
number that opens to 156 pictures*. **This is that problem with the sign
flipped** — there the format had no magic and here it had two letters nobody had
written down — and the method is the same one: put a guess to the whole
population at once and print where it does not close.

**`pc-1000miglia-doc`** — 1991, Simulmondo, Italian DOS, sixteen route filenames
read as a graph. **The precedent for reading a run of names as a structure**,
which `RESOURCE.FV1..FVN` is; [04](04-the-screens.md) reads it as a work list
rather than a graph, and says why.

## What a zero is worth here

`pc-popcorn-doc` is described in the index as *the lowest coverage here, 13.0927 %,
which is exactly its ceiling*. This object opened at **10.4611 %** — lower than
anything in the collection has started — and closed at **99.9775 % identified**,
because the 89.5163 points that were opaque turned out to be one format that
closes to residue zero twenty-three times.

**Those two sessions are the same problem with opposite answers, and the
difference is not effort.** `pc-popcorn`'s ceiling was its ceiling because its
opaque bytes were behind a decompressor. This object's opaque bytes were behind
a run-length rule that fits in four lines. **The lesson is that a low opening
figure says nothing at all about a closing one** — it says how much has not been
looked at yet, and here that turned out to be twenty-three pictures and a
hundred and four bytes with four names in them.
