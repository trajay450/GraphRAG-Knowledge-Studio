# Verified local execution report

Command: `python main.py`

Demo exit code: 0

```text
{
  "entities": [
    "computer vision",
    "deep learning",
    "external validation",
    "generalization",
    "image classification",
    "medical imaging",
    "privacy"
  ],
  "sources": [
    {
      "id": "d1",
      "text": "PyTorch supports neural network research and deep learning experiments."
    },
    {
      "id": "d2",
      "text": "Deep learning supports computer vision and image classification."
    },
    {
      "id": "d3",
      "text": "Computer vision can process medical imaging datasets."
    },
    {
      "id": "d4",
      "text": "Medical imaging datasets require privacy and careful external validation."
    },
    {
      "id": "d5",
      "text": "External validation tests generalization across institutions."
    }
  ],
  "abstained": false
}

```

Test exit code: 0

```text
test_abstain (test_core.TestCore.test_abstain) ... ok
test_citations (test_core.TestCore.test_citations) ... ok
test_graph_has_edges (test_core.TestCore.test_graph_has_edges) ... ok
test_import (test_core.TestCore.test_import) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK

```

These are local baseline results on synthetic or tutorial data, not external validation.
