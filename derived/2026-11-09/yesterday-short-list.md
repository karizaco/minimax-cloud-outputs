# Yesterday's short list — did it show up this morning?

**Source:** derived join of daily-screens/<prior>/tier-a.csv to the morning feed (no source file is modified) · **Built:** 2026-11-11 · **Covers:** 2026-11-09 morning, prior board 2026-11-06, 8 name(s) · read-only

> **Read this before the table.**
>
> This is a follow-up, not a demand that the two lists match. The evening
> list and the morning feed are different jobs. The question is whether
> yesterday's lead names were in this morning's feed at all, and whether
> any that were there were past the 3% line the morning brief treats as a gap.
>
> `gapping` means the morning print was at least 3% either way. `under the line`
> means the name was in a feed but the print was smaller than that.
> `not in the feed` means none of the morning feeds quoted the name. It does
> not mean the name was flat. It means nobody quoted it.

Prior board: `2026-11-06`.
Ticker column: symbol.
Feeds consulted: the pre-open tape (`preopen-feed/2026-11-09-0950.jsonl` and 1 earlier checkpoint(s)); the gap brief's 3% band (`ntrt/2026-11-09.csv`); the brief's own screen (`daily-briefs/2026-11-09-pre-market.csv`).

| Status | Names |
|---|---|
| gapping | 0 |
| under the line | 1 |
| not in the feed | 7 |

| Ticker | Yesterday's move | This morning | Status | Feed |
|---|---|---|---|---|
| XERS | +16.21% | +0.66% | under the line | the brief's own screen (`daily-briefs/2026-11-09-pre-market.csv`) |
| ACHC | +6.35% | — | not in the feed | no feed quoted it |
| APP | +9.86% | — | not in the feed | no feed quoted it |
| FUN | +8.23% | — | not in the feed | no feed quoted it |
| MRNA | +5.27% | — | not in the feed | no feed quoted it |
| RUN | +1.11% | — | not in the feed | no feed quoted it |
| SEZL | -3.59% | — | not in the feed | no feed quoted it |
| U | +5.51% | — | not in the feed | no feed quoted it |

A blank yesterday move means that board did not publish one. A blank morning
print means the name was not in the feed, which is the status, not a zero.
The feed column names where each print came from; a name quoted by more than
one feed is shown from the LATEST feed that quoted it, because "was it
gapping?" is answered by the most recent print.

