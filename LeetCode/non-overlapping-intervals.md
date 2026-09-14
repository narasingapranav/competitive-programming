# 🟠 non-overlapping-intervals — Non-overlapping Intervals

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/non-overlapping-intervals/) &nbsp;|&nbsp; **Solved:** 2026-02-26

---

## 📝 Summary

Accepted solution for Non-overlapping Intervals on LeetCode.

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
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        end=float('-inf')
        count=0
        for s,e in intervals:
            if s>=end:
                count+=1
                end=e
        return len(intervals)-count

```

</details>
