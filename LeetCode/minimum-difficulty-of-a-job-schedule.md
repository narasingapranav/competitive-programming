# 🟠 minimum-difficulty-of-a-job-schedule — Minimum Difficulty of a Job Schedule

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Accepted solution for Minimum Difficulty of a Job Schedule on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Dynamic programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n²) (estimated -- DP table detected)` | `~O(n) (estimated)` |

## 🏷️ Tags

`dp`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minDifficulty(self, a: List[int], d: int) -> int:
        n = len(a)
        if n < d:
            return -1
        dp = [[10000000] * (n) for _ in range(d + 1)]
        maxjob = 0
        for i in range(n):
            maxjob = max(maxjob, a[i])
            dp[1][i] = maxjob
        for day in range(2, d + 1):
            for i in range(day - 1, n):
                maxjob = 0
                for j in range(i, day - 2, -1):
                    maxjob = max(maxjob, a[j])
                    dp[day][i] = min(dp[day][i], dp[day - 1][j - 1] + maxjob)
        return dp[d][n - 1]

```

</details>
