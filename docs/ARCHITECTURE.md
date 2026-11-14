# Architecture

```mermaid
flowchart LR
    N0["Source passages"] --> N1["Entity extraction"]
    N1["Entity extraction"] --> N2["Graph construction"]
    N2["Graph construction"] --> N3["Multi-hop traversal"]
    N3["Multi-hop traversal"] --> N4["Cited evidence"]
```

## Module boundaries

Each stage is deliberately implemented as a compact, inspectable reference pipeline. No external production service is required for the demonstration.
