# 🟠 find-center-of-star-graph — Find Center of Star Graph

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-center-of-star-graph/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Accepted solution for Find Center of Star Graph on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nf=set(edges[0])
        ns=set(edges[1])
        return nf.intersection(ns).pop()
```

</details>
