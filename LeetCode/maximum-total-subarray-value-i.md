# 🟠 maximum-total-subarray-value-i — Maximum Total Subarray Value I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-total-subarray-value-i/) &nbsp;|&nbsp; **Solved:** 2026-06-09

---

## 📝 Summary

Accepted solution for Maximum Total Subarray Value I on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxTotalValue(self, A: List[int], k: int) -> int:
        return k*max(A) - k*min(A)
```

</details>
