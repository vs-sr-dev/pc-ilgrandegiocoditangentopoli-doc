# 04 — The screens: a thermometer for bribes, and a game that says everything it has to say in pixels

*Measure: `python tools/px.py --render --recurse iggdt --out _work/png --expect
23`, twenty-three PNG written, 23 of 23 at residue 0; `python tools/px.py
--render <file> --out _work/png --crop X,Y,W,H --zoom N` for every quotation
below; the census in `notes/px-census.txt`.*

*And one section of this chapter — **One witness** — is not a measurement and
says so in its first line. It is the only passage in this repository that is
not.*

---

**Twenty-three files decoded, twenty-three pictures written out, and every
sentence this game speaks is in them.** There is not one readable Italian string
anywhere in this object outside `INSTALL.BAT` — and there did not need to be,
because the writing is drawn. Menus, intro, prompts, win and lose, credits,
system requirements: all of it is paint.

That is the finding that reorganises the whole object. The pre-briefing's
reasonable expectation was that the game's text was inside 43,445 packed bytes
of `START.EXE` and that recovering it was the session's big prize. **It is not in
there. It is here, at 320 × 200, and it cost a run-length decoder to read.**

## What the game is

You are a magistrate. The game names him: **Giudice De Petris**, drawn in blue in
`RESOURCE.FVD`.

The intro is six pages of ruled notepaper with a court seal in the corner, and it
reads, in order:

> Ignobili personaggi hanno saccheggiato l'Italia dal 1945 fino a oggi.
> Ma negli ultimi 20 anni abbiamo visto i peggiori ladroni. Aiuta ▮ a vincere la
> dura battaglia di Tangentopoli. Non permettere ai grandi politici di
> intascarsi 💵 e di accaparrarsi 👑. Non farti distrarre dai ▮ e stai in
> guardia: ai lati del Palazzo del Potere crescono altre forze oscure, che dovrai
> combattere. E occhio al **TANGENTOMETRO**: devi evitare che tocchi il massimo
> prima del 1993. L'Italia confida in te: non deluderla!

*Ignoble characters have plundered Italy from 1945 until today. But in the last
20 years we have seen the worst thieves. Help ▮ win the hard battle of
Tangentopoli. Do not let the big politicians pocket 💵 and grab 👑. Do not be
distracted by ▮ and stay on your guard: at the sides of the Palace of Power
other dark forces are growing, which you will have to fight. And keep an eye on
the TANGENTOMETRO: you must stop it reaching maximum before 1993. Italy trusts
you: do not disappoint her.*

The ▮ are gaps in the paint where a sprite is composited at run time —
`RESOURCE.FV9` has three distinct colour indices in the whole 64,000 pixels,
which is a page of black text on white with a hole in it.

**And the last sentence of the intro is a date the object states about itself.**
*Devi evitare che tocchi il massimo prima del 1993* — the game's clock runs to
1993, not to 1996. [07](07-the-clocks.md) is about what that is worth.

## The Tangentometro, which is a thermometer

The title on the main board is a shop sign over a road, and under it hangs a
**mercury thermometer**:

```
python tools/px.py --render iggdt/RESOURCE.FV1 --out _work/png \
    --crop 100,20,140,30 --zoom 4
```

The empty thermometer is on the board. The filled one — a bar running green,
yellow, orange, red, violet — is a sprite in `RESOURCE.FVD` and appears again in
the intro page that warns about it and in the losing screen. **The bribe meter is
a fever chart**, and the joke is old enough that the game never explains it.

## The twenty-three, one line each

| file | bytes | idx | what is on it |
|---|---:|---:|---|
| `FV1` | 17,198 | 63 | **the board.** A wall with two arched gateways, a road with a dashed centre line, lawns, a lamp post, a bare tree, blue sky between the arches, and the `TANGENTOMETRO` sign with the empty thermometer under it. The only screen with its own palette. |
| `FV2` | 29,245 | 81 | sprite sheet, and the busiest one: **five frames of a magistrate throwing a sheet of paper**, seven close-up figures, five frames of a hand pulling a yellow folder out of an archive shelf, ivy-grown stone wall tiles, a brick column, stacks of ruled paper, a colour bar, and four panels — `VUOI ABBANDONARE L'INCHIESTA? S/N`, `AVVISO DI GARANZIA`, `DEMO`, `INCHIESTA SULLA MAGISTRATURA`. See below. |
| `FV3` | 26,114 | 38 | eight frames of the title animation — a vertical green-white-red column with letters tumbling down it — a `VUOI TORNARE AL DOS? S/N` panel, and **the credits** |
| `FV4` | 42,828 | 45 | **the title screen.** *il grande gioco di* in gold, `TANGENTOPOLI` in green, white and red, on a blue gradient, under two rows of small gold-and-red figures |
| `FV5` | 43,428 | 42 | the same screen **without the word** — the frame the animation lands on |
| `FV6` | 9,440 | 4 | intro 1 of 6, ruled paper and a seal |
| `FV7` | 11,415 | 28 | intro 2 of 6, with a judge-at-desk sprite set into the sentence |
| `FV8` | 9,583 | 16 | intro 3 of 6, with banknotes and a crown set into the sentence |
| `FV9` | 9,508 | **3** | intro 4 of 6 — black, white and one more, with a gap for a sprite |
| `FVA` | 9,342 | 18 | intro 5 of 6, with the filled `TANGENTOMETRO` set into the sentence |
| `FVB` | 6,772 | **3** | intro 6 of 6: *prima del 1993. L'Italia confida in te: non deluderla!* |
| `FVC` | 8,218 | 4 | five line-art court seals on ruled lines — the notepaper's letterhead, in stages |
| `FVD` | 13,073 | 68 | sprite sheet: a bald bespectacled grinning head in two frames, four figures carrying a red cross, judges seated at desks, the `TANGENTOMETRO` filled in two states, and **`Giudice De Petris`** |
| `FVE` | 12,844 | 32 | six wooden desks with a turned spiral in the front panel, and a fragment of `De Petris` left over from the sheet before it |
| `FVF` | 5,620 | 37 | a red-bordered board on orange between brick columns, embossed `AVVISI DI GARANZIA` |
| `FVG` | 30,019 | 55 | sprite sheet for the archive game: stone blocks, black spills, ovals, wooden doors, and three panels — `VUOI ABBANDONARE L'INCHIESTA? S/N`, `COMPLIMENTI! HAI RECUPERATO TUTTE LE PRATICHE`, `NON SEI RIUSCITO A RECUPERARE NEANCHE UNA PRATICA. I CORROTTI RINGRAZIANO...` |
| `FVH` | 38,976 | 34 | **`UFFICIO INCARTAMENTI`** — a teal room in perspective, a door on the left, and a large sand-textured floor grid. The biggest file, and it is big because the floor is noise. |
| `FVI` | 10,626 | 19 | the panels: `LIVELLO`, `PAUSA`, and `PRATICHE DISINSABBIATE` over a 2 × 4 grid of 100 … 800 |
| `FVJ` | 15,872 | 32 | a grey plaque with tricolour bars: `ONORE` / `A CHI S'OPPOSE COL PROPRIO FERMO CORAGGIO ALLA CORRUZIONE E AL DEGRADO D'ITALIA` |
| `FVK` | 7,080 | 31 | the losing screen: `L'INCHIESTA E' ARCHIVIATA`, the full thermometer, `LA CORRUZIONE DILAGA!`, `punteggio finale` |
| `FVL` | 19,414 | 40 | the winning plaque, with the Italian Republic's star-and-cogwheel emblem: `ONORE` / `AL MAGISTRATO CHE CON LE PROPRIE INDAGINI RIUSCI' A SRADICARE IL CANCRO DELLA CORRUZIONE, DONANDO NUOVA SPERANZA ALL'ITALIA` |
| `FVM` | 17,291 | 30 | the requirements panel: `cpu 286` / `cpu 386 e oltre` and `DOS 3` `4` `5` `6` with tick boxes, and `joystick non installato — attivata la modalita' di tastiera` |
| `FVN` | 19,048 | 14 | two joystick calibration panels: *posiziona il joystick in alto a sinistra / in basso a destra e premi il pulsante (altrimenti premi esc)* |

`idx` is the number of distinct palette indices the 64,000 pixels actually use,
of 256. **The lowest is three**, on two of the intro pages — a page of writing —
and the highest is eighty-one, on the sheet of magistrates.

## The vocabulary, which is the game's best joke and is not translatable

Three words carry it.

**`PRATICHE DISINSABBIATE`.** A *pratica* is a case file. *Insabbiare
un'inchiesta* — literally *to sand over an investigation* — is the standard
Italian idiom for burying one. So the score counter counts **case files
un-sanded**, and the room they are buried in, `UFFICIO INCARTAMENTI`, has a floor
drawn as a field of sand. The pun is built into the level art.

**`AVVISO DI GARANZIA`.** The notice of investigation that a prosecutor served on
a suspect, and in 1992 and 1993 the single most recognisable object in Italian
public life. In this game it is a pickup — `RESOURCE.FVF` is a whole screen for
a board of them, `AVVISI DI GARANZIA`, plural.

**`ARCHIVIATA`.** When you lose, the screen does not say game over. It says
*l'inchiesta è archiviata* — the investigation has been shelved — which is the
formal term for a case closed without charges, and then *la corruzione dilaga*,
corruption is running wild.

**A game whose failure state is the correct legal term for the thing everybody
was afraid of.** It is 1990s Italian satire compressed into two words on an
orange panel, and it is drawn rather than printed because in 1996 that was
cheaper than a font.

## The magistrate's hand

`RESOURCE.FV2` is the sheet the game actually runs on, and three of its animations
are worth reading frame by frame.

```
python tools/px.py --render iggdt/RESOURCE.FV2 --out _work/png \
    --crop 180,0,140,105 --zoom 4
```

**Five magistrates, and only four of them are holding anything.** A figure in a
black gown and a black *tocco*: one frame with both arms down and empty hands,
then four with a **white sheet of paper** in the raised hand, the arm at four
different heights and to either side. That is a throw cycle with an idle frame,
drawn once and mirrored by whatever draws it.

**What the white sheet is, said as an inference rather than as a reading.**
Nothing in the sprite spells it. But `RESOURCE.FVF` is an entire screen given
over to a board reading `AVVISI DI GARANZIA` — plural — and this same sheet
carries a panel reading `AVVISO DI GARANZIA` singular, a few dozen pixels from
the sprite. **A magistrate in a gown throwing single sheets of paper, on a sheet
that names the notice of investigation twice, is throwing notices of
investigation.** It is the strongest reading available and it is not a
measurement, so it is written here as what it is.

```
python tools/px.py --render iggdt/RESOURCE.FV2 --out _work/png \
    --crop 0,155,320,45 --zoom 3
```

**Seven close-up figures in a row along the bottom, and they are two
characters.** Five are one man — black gown over a grey suit, red tie, *tocco*,
a purple law code under the arm, and in the first frame a raised index finger.
Two are somebody else: fairer hair, black and a red tie, no gown over a suit and
no book. Which of them is `Giudice De Petris` — the name painted in blue in
`RESOURCE.FVD` — is not settled by either sheet, and this page will not guess.

```
python tools/px.py --render iggdt/RESOURCE.FV2 --out _work/png \
    --crop 0,148,150,22 --zoom 9
```

**And five frames of the archive.** A shelf of white ruled paper, twice; then a
bespectacled man leans in from the left and draws out a **yellow folder**, and in
the last frame there is a white burst where something scatters. That is
`PRATICHE DISINSABBIATE` at sprite scale — the case file coming back out of the
sand.

## One witness, and he is not a measurement

**Everything else in this repository is a count, and this section is not.** It is
kept because the object had no witnesses at all and now has one, and because
mixing the two kinds of evidence silently would be worse than marking the join.

The owner of this collection played this game as a small child, and remembers two
things about it: that `RESOURCE.FV1` — the wall, the two arched gateways, the
road with the dashed centre line and the `TANGENTOMETRO` sign — **was the arena**,
and that there was a hand that threw sheets of paper, or money, around it.

**Both are corroborated by the bytes, and neither was derived from the
recollection.** `FV1` was identified as the board a day earlier, from a palette
that no other screen in the object shares and from being the only one that needs
a sky. The hand was found afterwards, by going to look for it: it is the
five-frame magistrate above, and the sheet is white, not green — the game's
banknotes are drawn green in `RESOURCE.FV8`, and this is paper.

Two things follow that the bytes cannot say on their own.

**The game was distributed and it reached a household.**
[08](08-against-the-collection.md) reports 0 crossings of 26 over 108
repositories and no trace of the title on either Italian cover disc this
collection holds, and concludes that the route by which this game reached anybody
is unknown. It is still unknown. **But it reached somebody**, and that is now a
fact about the object rather than an assumption.

**And the satire landed on an audience it was not written for.** A child of four
or five saw a man in a black gown flinging bits of paper across a road and
found it funny, which is the entire experience available at that age. The bits
of paper were the *avviso di garanzia* — in 1993 the most recognisable piece of
stationery in the country, the thing that opened the evening news. **The joke
worked twice, at two completely different resolutions**, and the second one is
the reason anybody remembers it well enough to go looking for the files thirty
years later.

## What the numbering is not

`FV1` is the board and `FV4` and `FV5` are the title screen; the intro runs
`FV6`..`FVB`; the endings are `FVJ`, `FVK`, `FVL`; the system checks are `FVM`
and `FVN`. **The sequence is not presentation order.** It groups by kind —
board, sheets, title, intro, sprites, panels, plaques, setup — which is the order
an artist finishes things in and not the order a player meets them.

`pc-1000miglia-doc` is this collection's precedent for reading a run of file
names as a structure; there sixteen route names were a graph. **Here twenty-three
names are a work list.**

## The word `DEMO`, and what cannot be said about it

`RESOURCE.FV2` contains a panel with `DEMO` embossed on it. The header of
`START.EXE` says `V. 1.0`.

**Whether this build ever shows that panel is not determinable from the bytes**,
because deciding it means running the program and rule 3 forbids that. What can
be said is that the artwork for a demo marker shipped, that `INSTALL.BAT` looks
for a `LEGGIMI.DOC` that is not here, and that the high-score table has never
been played on. **Three signs of a copy that was distributed rather than used**,
and none of them is proof of a demo build.

## Twenty-three pictures out of eighty-nine and a half per cent

```
python tools/px.py --render --recurse iggdt --out _work/png --expect 23

opened                                   : 23 of 23
decoded with residue 0                   : 23 of 23
```

The PNG are not committed — this repository publishes `README`, `docs/`,
`notes/`, `tools/` and `.gitignore` — but the command that makes them is on this
page and it takes about a second.
