# 🟠 non-overlapping-intervals — Non-overlapping Intervals

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/non-overlapping-intervals/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Find the minimum number of intervals to remove from a list so that the remaining intervals do not overlap.

## 🔍 Key Observation

Maximizing the number of kept non-overlapping intervals is equivalent to the classic Activity Selection Problem, which can be solved by greedily picking intervals that end earliest.

## ⚙️ Algorithm

**Greedy (Interval Scheduling)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`greedy` `intervals` `sorting`

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
