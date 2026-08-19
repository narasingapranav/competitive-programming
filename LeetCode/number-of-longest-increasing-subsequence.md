# 🟠 number-of-longest-increasing-subsequence — Number of Longest Increasing Subsequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Given an integer array, return the number of longest increasing subsequences.

## 🔍 Key Observation

By keeping track of both the length of the longest increasing subsequence ending at each index and the count of such subsequences, we can update counts dynamically whenever a longer or equal-length subsequence is found.

## ⚙️ Algorithm

**Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n)` |

## 🏷️ Tags

`dynamic-programming` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        mx = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        mx = max(dp)
        res = 0
        for i in range(n):
            if dp[i] == mx:
                res += count[i]
        return res

```

</details>
