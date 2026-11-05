# SIP exit codes

| Code | Meaning |
|---:|---|
| 0 | Success. The requested operation completed and all required validation passed. |
| 2 | Usage or input error. A file was missing, unreadable, malformed, or the command was invoked incorrectly. |
| 3 | Minimax model failure. The draft command ran but the model did not produce a usable response. |
| 4 | Minimax infrastructure or provider failure. The draft command could not complete because of an external service, dependency, or execution problem. |
| 5 | Validation failure. The draft was produced, but it violated a required check such as the number trace. |
| 6 | Internal SIP failure. An unexpected internal error prevented the pipeline from completing. |
