# 🟠 longest-consecutive-sequence — Longest Consecutive Sequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/) &nbsp;|&nbsp; **Solved:** 2026-06-01

---

## 📝 Summary

Accepted solution for Longest Consecutive Sequence on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        maxlen=0
        for i in s:
            if i-1 not in s:
                j=i
                while j in s:
                    j+=1
                    maxlen=max(maxlen,j-i)
        return maxlen
```

</details>
