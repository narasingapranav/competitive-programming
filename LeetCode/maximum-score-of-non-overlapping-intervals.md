# 🟠 maximum-score-of-non-overlapping-intervals — Maximum Score of Non-overlapping Intervals

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/) &nbsp;|&nbsp; **Solved:** 2026-09-12

---

## 📝 Summary

Select at most 4 non-overlapping intervals from a given set to maximize the total weight, returning the chosen interval indices with lexicographical tie-breaking.

## 🔍 Key Observation

Sorting intervals by right endpoint allows finding the latest non-overlapping interval using binary search, reducing the problem to a 2D dynamic programming state over interval count (up to 4).

## ⚙️ Algorithm

**Dynamic Programming + Binary Search**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`dynamic-programming` `binary-search` `sorting` `intervals`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [
            (intervals[i][1], intervals[i][0], intervals[i][2], i)
            for i in range(n)
        ]
        # Sort by right endpoint.
        arr.sort(key=lambda x: x[0])

        dp = [[0] * 5 for _ in range(n + 1)]
        indices = [[[] for _ in range(5)] for _ in range(n + 1)]

        for i in range(n):
            r, l, weight, idx = arr[i]
            # Use binary search to find intervals whose right endpoints are smaller than l.
            k = bisect_left(arr, (l,), hi=i)

            for j in range(1, 5):
                s1 = dp[i][j]
                s2 = dp[k][j - 1] + weight
                if s1 > s2:
                    dp[i + 1][j] = dp[i][j]
                    indices[i + 1][j] = indices[i][j].copy()
                    continue

                new_index = indices[k][j - 1].copy()
                new_index.append(idx)
                new_index.sort()
                if s1 == s2 and indices[i][j] < new_index:
                    new_index = indices[i][j].copy()
                dp[i + 1][j] = s2
                indices[i + 1][j] = new_index

        return indices[n][4]
```

</details>
