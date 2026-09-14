# 🟠 combinations — Combinations

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/combinations/) &nbsp;|&nbsp; **Solved:** 2025-12-20

---

## 📝 Summary

Accepted solution for Combinations on LeetCode.

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
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a=[i for i in range(1,n+1)]
        c=combinations(a,k)
        l=list(i for i in c)
        return l
```

</details>
