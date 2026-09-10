# 09 — The box and the corrections: four tools, 273 checks, eleven things that were wrong, and one of them was mine

*Measure: `python tools/toolsdiff.py ../pc-rpgmakermv-doc/tools
--expect-differing 1`, in `notes/toolsdiff.txt`; `python tools/toolscan.py`, 572
files and three positive controls; `notes/selftests.txt`, 273 checks and 0
failures with `PYTHONIOENCODING` absent; `python tools/dirguard.py --survey
--tools tools` and `python tools/nameguard.py --survey --tools tools`, in
`notes/`; `python tools/refusals.py iggdt` and `python tools/refusalclass.py
notes/refusals.txt`; `python tools/rule0hook.py --report`, in `notes/rule0.txt`;
`python tools/pathcheck.py --needle <the collection directory's name>`; `python
_work/calib3.py --append -5.50`, in `notes/calibration.txt`.*

---

## § 1 — Rule 0, registered before a tool was touched, and it fired three times

`tools/rule0hook.py` travelled in the box; its registration did not.
`.claude/settings.local.json` was written **before the first line of the first
tool**, `.claude/` is in `.gitignore`, and the hook was proved live by being
made to refuse something:

```
$ python -c "print('this should be refused by rule 0')"
rule 0 (rule0hook.py): this command carries content through the shell --
inline program. write the program to a scratch .py file with the Write tool,
then run it.
```

```
python tools/rule0hook.py --report                     (notes/rule0.txt)

  REFUSED as rule-0 : 4
      heredoc               2
      inline program        1
      in-place edit script  1
```

**Four refusals, three different rules, and none of them reached the shell.**

The first two were deliberate: an inline program to prove the hook was live
before a tool was written, and a heredoc to prove it covered heredocs too.
**The last two were not.** The `sed -i` was the habit firing on a one-line edit
to a scratch file; the second heredoc was `git commit -F -` with the message
piped in, at the very end of the session, hours after the hook had been running
and after this chapter's own section on it had been drafted. **A rule that has
to be remembered is a rule that is forgotten while you are writing about
remembering it**, which is P16's whole argument arriving on schedule.

The denominator grows with every shell call and the numerator does not, so the
four are the measurement and the total — 127 calls at the moment
`notes/rule0.txt` was last written — is not.

## § 2 — Four tools written, one modified, 568 inherited

```
python tools/toolsdiff.py ../pc-rpgmakermv-doc/tools --expect-differing 1

mine   : 572 .py     theirs : 568 .py
only mine   : dosdis.py, dospack.py, px.py, tngscore.py
only theirs : none
common      : 568    differing   : 1
   DIFFERS  coverage.py
```

Every name was checked against `tools/` before it was written. `px.py` was free;
`pcx.py`, `palfit.py`, `palscore.py` and `palscoreraw.py` were not the same
thing. `hiscore.py` was free too and was **not** used, because `_work/hiscore.py`
already exists as a probe and two files with one name in one session is a
confusion that costs more than a longer name — hence `tngscore.py`.

| tool | checks | what it is for |
|---|---:|---|
| `coverage.py` | 101 | +6, for the `PX` magic and its four refusals |
| `px.py` | 38 | the `PX` reader, the palette, the crop |
| `dosdis.py` | 35 | a strict 8086 disassembler that stops rather than guesses |
| `dospack.py` | 21 | the MZ header, the relocator arithmetic, 33 signatures |
| `tngscore.py` | 20 | `HIGHSCOR.TNG`, and 512 keys narrowed in three stages |
| `rule0hook.py` | 26 | rule 0, as a program |
| `nameguard.py` | 13 | the shared name guard |
| `pathcheck.py` | 10 | rule 6, as a program |
| `dirguard.py` | 9 | the shared guard |
| **total** | **273** | **0 failures** |

**Every one of those was run with `PYTHONIOENCODING` deleted from the child's
environment**, not merely unset in the shell — `notes/selftests.txt` says so on
its first line, and the script that made it pops the variable rather than
trusting it to be absent.

And two tools were used this session and have **no selftest at all**:
`exepack.py` and `sigcount.py`. They are named in `notes/selftests.txt` rather
than left out, because a battery that quietly drops the untested tools reports a
cleaner box than it has.

## § 3 — The four new tools against the box's own standing defects

**`dirguard`.** 216 raised of 571, unchanged in absolute number from 216 of 567
on the previous object. **All four new tools are in the refused column**, which
is the point of the survey existing: last session two of six new tools had no
guard and the survey caught them.

**`nameguard`.** 7 of the 10 tools that emit a file name, unchanged. All four new
tools call `nameguard.guard()` first thing in `main()`.

**Selection by magic, not by extension.** `px.py --recurse` opens every candidate
and reads two bytes. In a flat folder holding 23 screens, one `.EXE` and one
`.TNG`, an extension filter would have worked by luck — which is exactly the
condition under which `mzcensus.py` has carried its `.EXE` glob for fourteen
objects.

**`refusals.py`**: 60 of 92 refused, and `refusalclass.py` splits them
**`argparse` 23 for the tenth time**, `oserror` 18, `format` 18, `exception` 1.
Tenth population, tenth identical 23.

**Fifteen readers with no population here**: no PNG, no Ogg, no MPEG-4, no
`.pak`, no JSON, no Marshal, no `.chm`, no shop. One line, once.

## § 4 — What `pathcheck.py` found

```
python tools/pathcheck.py --needle <the collection directory's name>

tracked files            : 605
text files checked       : 605
VIOLATIONS               : 2
   docs/09-...:10    docs/09-...:112
```

Rule 6 forbids this machine's absolute paths in any published file, **including
inside captured tool output under `notes/`** — and `notes/` here holds
twenty-four files of captured output. Every one was generated with relative paths
from the repository root for that reason, and every one of them was clean.

**Both violations were in this chapter, and both were the *Measure:* line and
the paragraph you are reading**, which had spelled the needle out in order to
document the command that looks for it. The checker fired on its own
documentation. The needle is now named rather than written, the run is clean at
0, and the positive control still fires on a planted line — which is the part
that makes the zero mean something.

---

## § 5 — Corrections

**C.1 — the 89.5389 % is the wrong denominator, and the table it comes from does
not add up.** The pre-briefing gives the twenty-three resources as 413,058 bytes
= 89.5389 % of the object, in `formats.txt`, in `object.txt` and in
`prompt.txt`. The twenty-three resources are **412,954 bytes = 89.5163 %**. The
difference is 104, which is `HIGHSCOR.TNG` exactly — it was counted in the
resource row *and* in its own row, and `formats.txt`'s four-row split therefore
sums to **461,421 against an object of 461,317**. Re-derived by counting:
`coverage.py tree --root iggdt`, decoded row.

**C.2 — the one byte of residue is not residue.** The format closes at
**64,778 = 10 + 768 + 64,000, residue 0, on 23 of 23 files**. The pre-briefing's
13-byte header was an artefact of the test that chose it: the preamble begins
`0xF7` = 247, so any header length leaving the preamble in the stream fails a
"first 768 bytes are all below 64" test however right it is. Thirteen also cuts
the run `FF 05 00` at raw offset 7 in half. Decoding from 6 yields exactly nine
more bytes and 64,769 + 9 = 64,778. [03](03-the-format.md), and `px.py
--selftest` asserts the arithmetic.

**C.3 — the palette table was one byte out of phase, and the corrected reading is
a stronger claim.** The pre-briefing prints entries 0 and 1 as both black and
entry 2 as magenta, and concludes that 42, 21 and 63 *are the EGA sixteen-colour
set in six-bit VGA values*. Read at the right offset the sixteen entries are the
**canonical IBM EGA sixteen in canonical order** — black, blue, green, cyan,
red, magenta, brown, light grey, dark grey, light blue, light green, light cyan,
light red, light magenta, yellow, white — on 23 of 23 files. A palette that
merely uses EGA values and a palette that *is* the EGA table are different
findings and the second is checkable.

**C.4 — `jnb +1Ah` is the failure branch.** `executable.txt` annotates it
*enough room → go on* and calls the print-and-exit path *the other path*. `cmp
ax, [0002]` sets the carry when `ax` is below the top of memory; `jnb` takes the
jump when it is **not**, which is when there is not enough room, and the target
`0129h` is `mov ah,9 / mov dx,132h / int 21h` — *Manca memoria*. The fall-through
is the relocator. [06](06-the-program.md).

**C.5 — `exepack.py` gets the right answer for the wrong reason.** Handed
`START.EXE` it prints `NOT EXEPACK: entry point 1048672 is outside the file`.
The file is 43,445 bytes and the real entry point is 96. The tool computes
`e_cs * 16 + e_ip + header` without sign-extending `e_cs`, and `e_cs` here is
`0xFFF0` = −16 paragraphs, which is what a self-relocating stub uses. **A
negative `e_cs` is not exotic — it is the normal shape of the exact file class
this tool exists to identify** — so the defect will bite on a real EXEPACK image
built the same way. `dospack.py` sign-extends and its selftest asserts that
`e_cs = 0xFFF0` with `e_ip = 0x100` and a 96-byte header gives an entry offset
of 96.

**C.6 — `sigcount.py` handed a file instead of a directory reports zeros.**
`python tools/sigcount.py <one file> --hex 5058` prints *files searched: 0*,
*0 of 0*, *0 occurrences* and exits 0. It is not an error and it does not
refuse: it walks the path as a tree, finds no entries, and reports a clean
nothing. **A check that cannot fire reads exactly like a check that fired and
found nothing**, which is the shape of defect `dirguard.py` was built for, with
the arguments the other way round — a tree tool handed a file rather than a file
tool handed a tree. The measurement in [08](08-against-the-collection.md) was
re-run against the containing directory. **The repair belongs in `dirguard.py`
as a `want_tree()` beside `want_file()`, and the class has one known instance,
which is not yet a class.**

**C.7 — the high-score key is `x ^ 0xFE`, one bit from the reading that was
published.** The pre-briefing's complement gives `SNCDSUN`, `FTFMHDMLN`,
`UHLNUIX`, `LHBIDMD` and says they are not names. Under `x ^ 0xFE` they are
`ROBERTO`, `GUGLIELMO`, `TIMOTHY`, `MICHELE`; the six `0xFE` are a score of
**six zero bytes**, not six `0x01`; and the filler is `$`, the DOS `AH=09`
terminator, not `%`. The reason the sweep missed it is on the record: it covered
the affine family `k - x` and the single mask `x ^ 0x80`, and never swept `x ^ k`
over all 256 keys. [05](05-the-names.md).

**C.8 — "this object names no author at all" is false.** It names four, twice.
`P.2` of `question.txt` lists *no publisher named, no author named* and every
tool that looks for a name returned zero, correctly, because there is no string
to find. The names are painted in `RESOURCE.FV3` and stored XORed in
`HIGHSCOR.TNG`. **What was true is that no author is named in any string**, and
the difference between that sentence and the one that was written is the whole
of [05](05-the-names.md).

**C.9 — "the game's text is inside `START.EXE` and will be the largest single
thing recovered" is false.** `P.5.3` and `executable.txt` §5 both put the game's
writing behind the packer and called it *the object's real content*. It is in the
twenty-three pictures — intro, menus, prompts, endings, credits, requirements.
The reasoning was sound and the conclusion was wrong for a reason worth keeping:
**both files were opaque, and it was assumed the text was behind the harder
one.**

**C.10 — the misfiling of `INSTALL.BAT`, measured and deliberately not
repaired.** `coverage.py` files it as *plain text, ASCII*; it is cp437, with
**302 bytes ≥ 0x80** including 252 × `0xCD` and 38 × `0xBA`, and **0 of those
302 are in the first 512 bytes**, which is all `_printable` reads. Not repaired
here, and the reason is a judgement rather than an oversight: the misfiling
moves **no byte between buckets** — both readings are `specified / plain text` —
while a repair that reads further than 512 bytes changes how every text file in
138 repositories is classified. **An object with exactly one text file is the
worst possible place to make that change**, and the right place is an object
where the classification actually decides something.

**C.11 — a bug of mine, in a tool I wrote this session, that my own selftest was
built to miss.** `dosdis.py` computed every branch target as *walk origin +
position in blob + displacement* instead of *this instruction's address + its
length + displacement*. The two are identical when the branch is the first
instruction in the range, and **every branch check in the first selftest put
exactly one instruction in the blob**, so twenty-nine checks passed on a
disassembler that mislabelled every jump after the first. It surfaced on the
object: `73 1A` at `010D` was printed as `jnb 136h` when the target is `0129h`,
and `0136h` is inside the string *Manca memoria*. The repair is one expression;
the four checks added with it all put padding in front of the branch, and a
fifth reproduces the object's own case by hand.

---

## § 6 — The hunch, scored in a paragraph as instructed

`_pre/question.txt` §P.7 wrote seven things down, unpriced. **Five right, two
wrong, and both wrongs were wrong in the same direction — the object gave up
more than was expected of it, never less.**

**(a) twenty-three legible 320 × 200 screens, one artist, two exceptions —
mostly right.** Twenty-three decoded at residue 0; three palettes at 19 / 3 / 1
as predicted. But **not all of them are screens**: `FV2`, `FVD`, `FVE` and `FVG`
are sprite sheets, which the hunch explicitly ruled out.

**(b) the leftover byte is structural, not a pixel — right, and it was better
than that.** It was not leftover at all; it is the first byte of a ten-byte
preamble and the format closes at zero.

**(c) not a named commercial packer, the stub is the authors' own, the
compression simple enough to read off the code — right on all three.** Thirty
countable signatures absent; 526 bytes disassembled at 100 % coverage; LZ77 with
prefix-coded lengths and a literal path that XORs with the bit counter.

**(d) the game's Italian text is inside `START.EXE` and will be the largest
single thing recovered — WRONG.** C.9.

**(e) `HIGHSCOR.TNG`'s four fields are not names in any encoding the next
session will find — WRONG.** They are the four authors' first names, one bit
from the published reading. C.7. **This is the largest single miss on the
list**, because it was stated as a strong negative.

**(f) the `Year` cell ends up 1996 on the mtime alone, the weakest witness this
index has accepted — right on the answer, wrong on "alone".** The object states
*prima del 1993* in its own intro and lists DOS 3 to 6 in its requirements
panel; the mtime is still the only witness that dates the *artefact*, and
[07](07-the-clocks.md) argues the cell on exactly that ground.

**(g) coverage above 90 % if the reader is written, 10.4611 % if not, no middle
— right on the shape, and it landed at 99.9775 %.**

## § 7 — The calibration term

The series convention is **predicted minus obtained**, so a negative term is
under-claiming. This session prices nothing, so the term is a by-eye estimate
and is labelled as one.

**What I expected to find**, reading the pre-briefing before touching anything:
the twenty-three screens would open and be worth a chapter; `START.EXE` would
stay shut and that would be fine; `HIGHSCOR.TNG` would stay shut; the object
would remain anonymous; the coverage figure would land somewhere in the low
nineties. On a nominal twenty-four-point scale that is about **17**.

**What I found:** the screens opened *and* turned out to hold the game's entire
text; the residue closed to zero instead of staying at one; the high-score table
opened and gave four names; a credits screen gave four more; the object gave
itself an internal date; coverage landed at 99.9775 %. `START.EXE` stayed shut,
as expected, and stayed shut for a *better* reason than the one predicted. That
is about **22**.

**The term is −5.50.** `python _work/calib3.py --append -5.50` checks the
inherited series' eight claims — 0 wrong of 8 — and appends:

```
terms 38   sum -41.93   mean -1.1034   negative 26   positive 11   zero 1
last10 -47.30, mean -4.7300   tail run of negatives: 7
-5.50 ranks 12 of 38 by absolute value
```

**Seven consecutive negative terms.** The pipeline has now under-claimed eight
sessions running, and this one under-claimed for the most specific reason yet:
it assumed that what is hard to open is where the good material is. It was in
the easy file.

## § 8 — P20, P21 and P22, in declared pause

Three prescriptions inherited from the six-object family are **not exercised
here and are not abandoned**. They are written for an object with an ancestor,
a successor and a priced clause set, and this object has none of the three: no
family, no crossings, 26 files.

* **P20** — membership of the regression set. Not exercised: there is no prior
  object of this producer to regress against.
* **P21** — the per-clause counts. Not exercised: there are no clauses.
* **P22** — the list carried forward from `pc-rpgmakermv-doc/docs/12`. Not
  exercised: its items are about a publisher's carry-over between products.

**All three remain in force for the next object that has the shape they were
written for.**

## § 9 — What this session did not measure

* the two decode tables at `020E` and `0234`, read as tables ([06](06-the-program.md));
* the bit assignment of the LZ77 stream, and therefore its 361,680 bytes;
* the meaning of the `PX` preamble's first three words, and of `FV`;
* whether this build displays the `DEMO` panel that ships in `RESOURCE.FV2`;
* whether `Giudice De Petris` is a deliberate near-miss of a real name;
* three of the four sprite sheets, read as sprite sheets — extents, frame
  counts, hot spots. `FV2` was read in [04](04-the-screens.md) after a player's
  recollection sent somebody looking for one particular sprite, and it gave up
  three animations at once; `FVD` alone holds at least six distinct subjects and
  nobody has cut it up. **The lesson is not subtle: the sheet that was read is
  the sheet somebody had a reason to look at**, and the other three are waiting
  for a reason;
* `dos-platformnotes-doc`, which exists in this collection and was not consulted;
* whether *Il grande gioco di Tangentopoli* appears by name on any dated
  distribution anywhere, which is the one measurement that would settle
  [07](07-the-clocks.md) and is not a measurement of these bytes.
