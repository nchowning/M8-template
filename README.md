# M8-template
My M8 template save file config

## Template Version
The template version is specified on track 1 row F0. If you hold `Option` and `Down`, once you reach the bottom, the version will be on the top left (represented via a Chain - `01` for example). Other reserved Chains are placed in song rows `FD-FF`.

## Chains
I generally have 4 or 8 rows in my chains. Lately, I've been mostly using 4 row chains.

- `00`: Either 4 or 8 rows of Phrase `00` - depending on the song
- `01`: First row is Phrase `01`. The remaining rows are Phrase `00`. Either 4 or 8 rows - depending on the song
- `02-EF`: Available to use
- `F0`: Placeholder row for Phrases `F0-F7` which contain reserved tables
- `F1-F8`: Reserved for future use
- `F9`: 1 row or Phrase `00`
- `FA`: 1 row of Phrase `01`
- `FB`: 2 rows. First row is Phrase `01`. Remaining rows are Phrase `00`
- `FC`: 4 rows. First row is Phrase `01`. Remaining rows are Phrase `00`
- `FD`: 8 rows. First row is Phrase `01`. Remaining rows are Phrase `00`
- `FE`: 16 rows. First row is Phrase `01`. Remaining rows are Phrase `00`

## Phrases
- `00`: Empty Phrase
- `01`: `KIL` commands on row 1
- `F0`: Contains reserved Tables `80-8F`
- `F1`: Contains reserved Tables `90-9F`
- `F2-F5`: Reserved for future use
- `F6`: Contains reserved Tables `E0-EF`
- `F7`: Contains reserved Tables `F0-FF`
- `F8-FE`: Reserved for future use

## Tables
`tables.txt` contains a txt representation of all reserved tables

- `00-7F`: Reserved for instruments
- `80-8F`: Major chord arps
- `90-9F`: Minor chord arps
- `A0-DF`: Available to use
- `E0-EF`: Downward pitch bends
  - `E0-E3`: 2-note bend on row `02`
  - `E4-E7`: 2-note bend on row `01`
  - `E8-EB`: 1-note bend on row `02`
  - `EC-EF`: 1-note bend on row `01`
- `F0-FF`: Updward pitch bends
  - `F0-F3`: 2-note bend on row `02`
  - `F4-F7`: 2-note bend on row `01`
  - `F8-FB`: 1-note bend on row `02`
  - `FC-FF`: 1-note bend on row `01`

## Instruments
The current version of this template has some basic instruments (mostly drums) but nothing has been formalized yet.
