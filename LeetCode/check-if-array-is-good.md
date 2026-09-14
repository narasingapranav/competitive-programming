# 🟠 check-if-array-is-good — Check if Array is Good

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-if-array-is-good/) &nbsp;|&nbsp; **Solved:** 2026-05-14

---

## 📝 Summary

Accepted solution for Check if Array is Good on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n=nums[-1]
        return nums == list(range(1,n+1)) + [n]
```

</details>
