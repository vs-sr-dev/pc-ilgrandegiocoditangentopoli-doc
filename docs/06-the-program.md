# 06 — The program: forty-three kilobytes nobody signs, and a decision about how far to go in

*Measure: `python tools/dospack.py --selftest`, 21 checks; `python
tools/dospack.py iggdt/START.EXE --sweep --relocator`, in `notes/dospack.txt`;
`python tools/exepack.py iggdt/START.EXE`, in `notes/exepack.txt`; `python
tools/dosdis.py --selftest`, 35 checks; `python tools/dosdis.py iggdt/START.EXE
--at 96 --length 51 --org 0x100 --targets` and `--at 164 --length 526 --org 0
--targets`, in `notes/dosdis-entry.txt` and `notes/dosdis-stub.txt`.*

---

One executable, 43,445 bytes, no slack, one relocation, and `pecensus.py`
reports **format `n/a`** — a plain DOS MZ with no PE header, so no COFF
timestamp, no version resource, no `CompanyName`. Every clock this pipeline
normally reads off a binary is absent.

It asks the loader for **318,704 bytes more than it is** and its first
instructions are a hand-written relocator with an Italian error message. It is
packed, and thirty signatures say nothing about by what.

## The header, which is not padded with padding

A DOS header is `0x1C` bytes of declared fields and then whatever the linker
leaves before the relocation table. This one puts a sentence there:

```
bytes 0x1C .. 0x51, 54 bytes, ending exactly where the relocation table
begins at 0x52:

    0C 01   TANGENTOPOLI - V. 1.0 - (Perche' guardi qua dentro?)
    ^^^^^   ^-- 52 characters
```

**Fifty-two characters in fifty-two bytes of gap.** The author measured the hole
and wrote a sentence to fit it. It carries the object's only version number —
`V. 1.0` appears nowhere else — and it is addressed to whoever opens the file in
a hex editor.

`dospack.py` checks the fit rather than asserting it: *it ends exactly at the
relocation table: True.*

## Thirty signatures, and the pc-popcorn lesson kept as a column

`pc-popcorn-doc` is this collection's precedent: an Italian DOS game whose
EXEPACK image was found only after eight signature searches failed. Its lesson
is in `exepack.py`'s own docstring and it is sharper than "search harder":

> Seven of those eight are strings a packed file really does contain. The eighth
> is not. `EXEPACK` is the name of Microsoft's tool; it appears in the tool, not
> in its output.

So `dospack.py` records for every signature **where it is supposed to be**, and
marks the ones that name a compressor rather than appearing in its output as
`tool-only` and excludes them from the denominator. Counting them would inflate
a zero.

```
signatures in the table       : 33
  of those, tool-only         : 3
  countable                   : 30
  found ANYWHERE              : 0 of 30
  found IN THE RIGHT PLACE    : 0 of 30
```

LZEXE 0.90 and 0.91, PKLITE in three forms, EXEPACK by position and by error
string, DIET twice, TINYPROG, WWPACK, PROPACK twice, UPX twice, aPACK, aPLib,
LZPAK, SCRNCH, COMPACK, AINEXE, CRUNCHER, ExeShield, PGMPAK, RELOX, SHRINK, and
for good measure the Borland, Turbo Pascal and Microsoft C runtime banners.
**Thirty countable, thirty absent.**

And the positional test, which is the one that actually caught `pc-popcorn`:

```
python tools/exepack.py iggdt/START.EXE
  NOT EXEPACK: entry point 1048672 is outside the file
```

It reaches the right verdict for the wrong reason and
[09](09-the-box-and-the-corrections.md) C.5 says why.

**"Thirty signatures absent" does not mean "not packed."** `e_minalloc` demands
318,704 bytes, the image is 7.8152 bits per byte over all 256 values, and the
entry point is a relocator. It means the packer is one this table does not name,
or it is the authors' own.

## The entry stub, twenty-five instructions

```
python tools/dosdis.py iggdt/START.EXE --at 96 --length 51 --org 0x100 --targets

  0100  b8 4d 58       mov    ax, 584Dh     ; 22605 paragraphs = 361,680 bytes
  0103  ba 96 0a       mov    dx, 0A96h
  0106  05 00 00       add    ax, 0h        ; <- the file's one relocation
  0109  3b 06 02 00    cmp    ax, [2h]      ; the PSP's top-of-memory word
  010D  73 1a          jnb    129h          ; NOT ENOUGH ROOM -> complain
  010F  2d 20 00       sub    ax, 20h
  0112  fa             cli
  0113  8e d0          mov    ss, ax        ; a 512-byte stack at the top
  0115  fb             sti
  0116  2d 25 00       sub    ax, 25h
  0119  8e c0          mov    es, ax
  011B  50             push   ax
  011C  b9 26 01       mov    cx, 126h      ; 294 words
  011F  33 ff          xor    di, di
  0121  57             push   di
  0122  be 44 01       mov    si, 144h
  0125  fc             cld
  0126  f3 a5          rep    movsw         ; copy itself out of the way
  0128  cb             retf                 ; and far-jump into the copy
  0129  b4 09          mov    ah, 9h
  012B  ba 32 01       mov    dx, 132h      ; "Manca memoria    $"
  012E  cd 21          int    21h
  0130  cd 20          int    20h

bytes decoded : 51 of 51    coverage 100.0000 %
branch targets in range : 1     landing on a boundary : 1 of 1
```

**`jnb 129h` is the failure path, not the success path.** `cmp ax, [2]` sets the
carry when `ax` is below the top of memory; `jnb` takes the jump when it is
not, which is when the program needs more memory than exists. The pre-briefing
annotates the same instruction *enough room → go on*, which is the branch
inverted. [09](09-the-box-and-the-corrections.md) C.4.

The single relocation is at file offset 0x0007 — the immediate of `add ax, 0h`
— so the loader writes the load segment into it and `ax` becomes the paragraph
just past the unpacked image.

## The relocator's destination, computed

The pre-briefing listed this among the things it had not measured. It is
arithmetic, and `dospack.py --relocator` does it by *recognising* the move
rather than assuming it — no `rep movsw` of the right shape, no number:

```
words copied        294
bytes copied        588
source, in DS       0x0144
FILE RANGE          164 .. 751
```

`DS` is the PSP at entry and the image begins at `PSP:0100`, so an offset in
`DS` maps to a file offset by subtracting `0x100` and adding the 96-byte header.
**The decompressor is file offsets 164 to 751, 588 bytes, 1.3534 % of the
file** — and knowing that turns "there is an unpacker in here somewhere" into a
range you can hand to a disassembler.

## Five hundred and twenty-six bytes, decoded, and how much that is worth

`dosdis.py` is a 16-bit 8086 disassembler that **stops** on any opcode not in
its table. A permissive disassembler prints `db 0x8F` and carries on, and the
reader cannot tell a correct listing from one that lost the instruction boundary
three bytes ago. This one refuses, so a listing that reaches the end of its range
is a listing every byte of which a table entry decoded.

```
python tools/dosdis.py iggdt/START.EXE --at 164 --length 526 --org 0 --targets

bytes decoded : 526 of 526    instructions : 290    coverage 100.0000 %
STOPPED       : no -- every byte in range decoded
branch targets in range : 54     landing on a boundary : 54 of 54
```

**Fifty-four branch targets and fifty-four instruction boundaries.** That is the
check against the failure mode a disassembler cannot see: a listing whose jumps
all land where instructions start is a listing whose boundaries are probably
right. Handed the whole 588 bytes it stops at offset 587 — because the last 62
bytes are **not code**.

## What the 588 bytes do

**Offsets 0000–0034 — move the packed image out of the way.** `std`, then a
loop that copies the payload upward in 64 KB blocks, `dh` counting the blocks
out of `dx` (which the entry stub loaded with `0A96h` and never used until now).

**Offsets 0035–020D — the decompressor.** `ds` is set to the moved payload,
`es:di` to `0100h` in the destination, and then:

```
  003F  ad             lodsw                ; a 16-bit bit buffer, in bp
  0040  95             xchg   ax, bp
  0041  ba 10 00       mov    dx, 10h       ; sixteen bits left in it
  ...
  0080  d1 ed          shr    bp, 1         ; take one bit
  0082  4a             dec    dx            ; DEC does not touch the carry
  0083  74 f1          jz     76h           ; buffer empty -> refill
  0085  73 f5          jnb    7Ch           ; bit 0 -> another literal
```

It is an **LZ77 with a prefix-coded length and distance**: match lengths and
distance classes are read bit by bit and resolved through two byte tables that
live at `020E` and `0234`, indexed from four sites in the code — `[bx+20Eh]`,
`[bx+219h]`, `[bx+224h]`, `[bx+234h]`, all four inside the 62 bytes the listing
declined to decode. **The code's own table references confirm the code/data
split independently of the disassembler.** Matches are copied in place with
`rep movsb` from `di - bx`.

**Offsets 01CB–020D — the epilogue.** A run-length-coded relocation list is
walked and `bx` added to each `[di]`; then `ss:sp` and `cs:ip` are restored from
the tail of the stream and the unpacker far-returns into the unpacked program
with **every register zeroed**.

And one instruction in the literal path is worth its own line:

```
  007C  ac             lodsb
  007D  32 c2          xor    al, dl        ; <- the running bit counter
  007F  aa             stosb
```

**A literal is not copied. It is XORed with `dl`, which at that moment is how
many bits are left in the buffer** — a value that walks down from 15 to 1 as
consecutive literals are emitted. A stock decompressor's literal path is
`lodsb; stosb`. This one is not, which is a concrete difference from any
off-the-shelf build and a reason a generic unpacker pointed at this file would
produce sixty-four kilobytes of nonsense without complaining.

## The decision, and it is that this stops here

A thirteenth signature search cost nothing and thirty of them cost nothing. An
unpacker costs a great deal. The prompt asked for a decision and this is it,
with the reason attached.

**The reason the unpacker was worth writing has gone.** The pre-briefing's case
for going into `START.EXE` was explicit and correct as far as it went:

> There is no Italian text anywhere in this object except in `INSTALL.BAT`. A
> game called *Il grande gioco di Tangentopoli* has writing in it, and the
> writing is in the only place left: inside 43,445 packed bytes. **That is the
> object's real content and it is behind one stub.**

**It is not behind the stub.** It is drawn, at 320 × 200, in the twenty-three
resources — the intro, the menus, the prompts, the win, the lose, the credits,
the requirements ([04](04-the-screens.md)). The names are drawn too, and stored
a second time in 104 bytes ([05](05-the-names.md)). What is left inside
`START.EXE` is the game's *logic* — sprite placement, collision, scoring, the
Tangentometro's rate — and none of that is a sentence anybody can read.

**What would close the question, precisely.** Two routes and no third:

1. **Implement the decoder.** 290 instructions are on the page and their
   semantics are 8086; the two tables are 62 bytes; the literal XOR is one
   instruction. It is an afternoon's work and it is *reading*, not running.
   What it buys is 361,680 bytes of 8086 machine code with no symbols — which
   would then want a disassembler run over a third of a megabyte to say
   anything about.
2. **Execute or emulate the stub.** Rule 3 forbids it, so this route is closed
   regardless of cost.

Route 1 is affordable and its payoff is a third of a megabyte of anonymous code.
**That is a worse use of a session than the twenty-three pictures were**, and
the object agrees: it put its text in the pictures. The stub is measured to
588 bytes, disassembled to 526, characterised to the level of *LZ77, prefix-coded,
literals XORed with a running counter*, and left running.

## What is still not measured here

* the two tables at `020E` and `0234`, read as tables rather than as 62 bytes;
* the exact bit assignment — how many bits a length costs, how many a distance;
* `int3f = 1`: one `INT 3Fh` in the file, the Microsoft overlay interrupt,
  which may be nothing;
* the two bytes at `0x1C`, `0C 01` = 268, sitting between the last declared
  header field and the message;
* what `0A96h` in the entry stub is besides the block count it is used as.
