# 🟠 insert-interval — Insert Interval

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/insert-interval/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given a sorted list of non-overlapping intervals, insert a new interval into the list and merge any overlapping intervals.

## 🔍 Key Observation

Appending the new interval to the existing list and re-sorting allows the problem to be reduced to the standard interval merging technique.

## ⚙️ Algorithm

**Sorting + Greedy Merging**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`array` `sorting` `intervals`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                res[-1][1]=max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        return res
```

</details>
