# 🟠 non-overlapping-intervals — Non-overlapping Intervals

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/non-overlapping-intervals/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Find the minimum number of intervals that must be removed from a given array of intervals to ensure the remaining intervals do not overlap.

## 🔍 Key Observation

To maximize the number of non-overlapping intervals retained, always greedily choose the interval that finishes earliest.

## ⚙️ Algorithm

**Greedy interval scheduling**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`greedy` `sorting` `intervals`

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
