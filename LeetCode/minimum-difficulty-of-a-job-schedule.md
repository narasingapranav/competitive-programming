# 🟠 minimum-difficulty-of-a-job-schedule — Minimum Difficulty of a Job Schedule

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Partition an array of job difficulties into d contiguous non-empty days such that the total sum of each day's maximum difficulty is minimized. Return -1 if there are fewer jobs than required days.

## 🔍 Key Observation

The optimal schedule up to job i on day d can be found by iterating backward from job i to consider all valid start positions for the d-th day, maintaining the running maximum job difficulty.

## ⚙️ Algorithm

**Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(d * n^2)` | `O(d * n)` |

## 🏷️ Tags

`dynamic-programming` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minDifficulty(self, a: List[int], d: int) -> int:
        n = len(a)
        if n < d:
            return -1
        dp = [[10000000] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0
        for day in range(1, d + 1):
            for i in range(day, n + 1):
                maxjob = 0
                for j in range(i - 1, day - 2, -1):
                    maxjob = max(maxjob, a[j])
                    dp[day][i] = min(dp[day][i], dp[day - 1][j] + maxjob)
        return dp[d][n]

```

</details>
