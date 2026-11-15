# Yesterday's short list — did it show up this morning?

**Source:** derived join of daily-screens/<prior>/tier-a.csv to the morning feed (no source file is modified) · **Built:** 2026-11-15 · **Covers:** 2026-11-13 morning, prior board 2026-11-12, 4 name(s) · read-only

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

Prior board: `2026-11-12`.
Ticker column: symbol.
Feeds consulted: the pre-open tape (`preopen-feed/2026-11-13-0950.jsonl` and 1 earlier checkpoint(s)); the gap brief's 3% band (`ntrt/2026-11-13.csv`); the brief's own screen (`daily-briefs/2026-11-13-pre-market.csv`).

| Status | Names |
|---|---|
| gapping | 1 |
| under the line | 1 |
| not in the feed | 2 |

| Ticker | Yesterday's move | This morning | Status | Feed |
|---|---|---|---|---|
| NBIS | -16.84% | -3.91% | gapping | the pre-open tape (`preopen-feed/2026-11-13-0950.jsonl` and 1 earlier checkpoint(s)) |
| CRWV | -6.86% | -0.95% | under the line | the pre-open tape (`preopen-feed/2026-11-13-0950.jsonl` and 1 earlier checkpoint(s)) |
| AXGN | -5.51% | — | not in the feed | no feed quoted it |
| SHAZ | -8.06% | — | not in the feed | no feed quoted it |

A blank yesterday move means that board did not publish one. A blank morning
print means the name was not in the feed, which is the status, not a zero.
The feed column names where each print came from; a name quoted by more than
one feed is shown from the LATEST feed that quoted it, because "was it
gapping?" is answered by the most recent print.

