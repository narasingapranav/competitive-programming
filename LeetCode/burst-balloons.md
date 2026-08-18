# 🟠 burst-balloons — Burst Balloons

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/burst-balloons/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Find the maximum coins obtained by bursting all balloons, where bursting a balloon yields coins equal to the product of its value and the values of its current adjacent balloons.

## 🔍 Key Observation

Reverse the process and choose which balloon to burst LAST in a given subrange; this ensures that the boundary balloons remaining outside the range are fixed, decoupling the subproblems.

## ⚙️ Algorithm

**Interval Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^3)` | `O(n^2)` |

## 🏷️ Tags

`dynamic-programming` `interval-dp` `memoization`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        nums.insert(0, 1)
        @cache              # range in which we want to choose the last balloon to burst.
        def dp(start, end): # we know anything outside the range lasts "longer", as we determined it will burst later
            maxi = -(2 ** 31)
            if end < start:
                return 0
            for i in range(start, end + 1):
                maxi = max(maxi, dp(start, i - 1) + dp(i + 1, end) + nums[start - 1] * nums[i] * nums[end + 1])
            return maxi
        return dp(1, n)
```

</details>
