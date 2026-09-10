# 07 — The clocks: a file system, a sentence in a picture, and a list of DOS versions

*Measure: `python tools/mtimes.py iggdt --waves`, in `notes/mtimes.txt`; `python
tools/pecensus.py iggdt`; `python tools/px.py --render iggdt/RESOURCE.FVB` and
`iggdt/RESOURCE.FVM`; `python tools/dospack.py iggdt/START.EXE`.*

---

This object has to go in `pc-gamelist-doc` with a `Year` in the cell, and the
question of what to put there is not a lookup. It is an argument, and the
witnesses disagree in an interesting way.

## Every clock this pipeline usually reads, and it is absent

| clock | value |
|---|---|
| copyright string | none |
| COFF timestamp | none — `pecensus.py` reports format `n/a`, a plain MZ |
| version resource | none |
| readme | `LEGGIMI.DOC` is looked for by the installer and is not here |
| build path | `sift.py --group buildpath`: 0 and 0 |
| UUID | `uuidscan.py`: 0 version-1 UUIDs |
| e-mail address | `sift.py --group personal`: 0 in every row |
| ZIP / archive member dates | there is no archive |

**Six clocks, six absences, and all six controls behaving.** The only version
number in the whole object is `V. 1.0`, in fifty-two bytes of DOS header
padding, and a version number is not a date.

## Witness one: the file system, and it says 1996

```
python tools/mtimes.py iggdt --waves

wave 1   1996-12-24 23:32:00 .. 1996-12-24 23:32:00
         26 files   461317 bytes   100.00%
```

**One wave, to the second, over twenty-six files.** That is a directory record
and nothing more. It records the moment somebody wrote these files onto this
medium; it does not record when the program was written, and it is the weakest
witness this index has ever been asked to accept.

`pc-rpgmakermv-doc/docs/08` drew the distinction the previous object needed:
a copyright field is *an attribution rather than a derivation*. **A file system
mtime is a notch below that again** — it is neither. It is a fact about a copy.

And it is Christmas Eve at half past eleven at night, which is a fact about a
copy that is hard not to enjoy.

## Witness two: the game, and it says 1993

The last page of the intro, painted into `RESOURCE.FVA` and `RESOURCE.FVB`:

> E occhio al TANGENTOMETRO: devi evitare che tocchi il massimo **prima del
> 1993**.

*You must stop it reaching maximum before 1993.* That is the game's own clock,
inside its own fiction, and a game whose win condition is set at 1993 was
conceived when 1993 was the future or the present. The page before it says
*negli ultimi 20 anni* — in the last twenty years — counting back from a now
that the game does not otherwise name.

Tangentopoli began in February 1992. **The fiction is a 1992-or-1993 fiction and
the file system is 1996**, and those are not the same claim about the same
thing.

## Witness three: the requirements panel, and it says DOS 3 to 6

`RESOURCE.FVM` is a system-check screen with tick boxes:

```
cpu 286   [ ]        DOS 3  [ ]
cpu 386   [x]        DOS 4  [ ]
 e oltre             DOS 5  [ ]
                     DOS 6  [ ]
```

**Four DOS versions, ending at 6.** MS-DOS 6.0 shipped in March 1993 and 6.22 in
June 1994; Windows 95 shipped in August 1995 and is not on this panel, nor is
DOS 7. A requirements screen drawn in late 1996 that stops at DOS 6 and offers a
286 as its floor is a requirements screen drawn earlier than late 1996.

This is the weakest of the three as evidence — a panel can go unrevised — but it
points the same way as the intro and away from the mtime.

## What goes in the `Year` cell, and why

**1996**, and the row says what that is.

The reasoning, since it is not obvious:

* The `Year` column of `pc-gamelist-doc` records what an object can be shown to
  be, from the object. **The only witness that dates the artefact rather than
  the fiction is the mtime**, and it says 1996 on 26 files of 26.
* *prima del 1993* dates the **story**, not the build. A game can be set in a
  year it was not written in — this one is set in a year it was certainly not
  *sold* in, since the investigations it satirises were still running.
* The DOS list constrains the build loosely and contradicts nothing.

So: 1996, on a file system, and the row must say **file system** rather than
leaving a bare number to look like a copyright date. **This is the weakest
witness this index has accepted for a `Year`, and the honest form of the cell is
one that admits it.**

## The interesting version of the question, which stays open

Between the fiction's 1993 and the medium's Christmas Eve 1996 there are three
or four years, and the object gives no way to divide them. Three readings fit
every byte here equally well:

1. written in 1992–93 and released late, when the subject was already cooling;
2. written in 1992–93, released then, and this particular copy is a 1996
   re-packaging for a magazine cover disc or a shareware collection;
3. written in 1996 as a period piece about events four years old.

**The third is the least likely and is not excluded.** Nothing in 461,317 bytes
chooses. The `V. 1.0` in the header padding is consistent with all three.

The route to closing it is not in these bytes: it is a dated distribution —
a cover disc, a shareware catalogue, a magazine — and
[08](08-against-the-collection.md) went looking in the two the collection holds
and did not find it.
