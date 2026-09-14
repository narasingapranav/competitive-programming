# 🟠 minimum-operations-to-make-array-values-equal-to-k — Minimum Operations to Make Array Values Equal to K

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/) &nbsp;|&nbsp; **Solved:** 2025-09-04

---

## 📝 Summary

Accepted solution for Minimum Operations to Make Array Values Equal to K on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        l=set()
        for i in nums:
            if i<k:
                return -1
            l.add(i)
        return (len(l) - (1 if min(l)== k else 0))
```

</details>
