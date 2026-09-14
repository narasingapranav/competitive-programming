# 🟠 words-within-two-edits-of-dictionary — Words Within Two Edits of Dictionary

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/words-within-two-edits-of-dictionary/) &nbsp;|&nbsp; **Solved:** 2026-04-22

---

## 📝 Summary

Accepted solution for Words Within Two Edits of Dictionary on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
import numpy as np

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        N = len(queries[0])
        q_vec = np.array([[ord(c) for c in w] for w in queries], dtype=np.int8)
        d_vec = np.array([[ord(c) for c in w] for w in dictionary], dtype=np.int8)
        results = []
        for i in range(len(queries)):
            diff = q_vec[i] != d_vec
            edit_counts = np.sum(diff, axis=1)
            if np.any(edit_counts <= 2):
                results.append(queries[i])
                
        return results        
```

</details>
