# SIP exit codes

| Code | Meaning |
|---:|---|
| 0 | Success |
| 2 | Usage error, invalid input, configuration error, unsafe output path, or other Minimax input/other error |
| 3 | Minimax quota exhausted |
| 4 | Minimax rate limited |
| 5 | Number-trace validation failed, empty Minimax draft, or draft validation failed |
| 6 | Adapter failure or internal hard failure |

Routine operation must fall back on **any nonzero exit code**. A failure must not
silently become a successful run.
