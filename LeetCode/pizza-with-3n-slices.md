# 🟠 pizza-with-3n-slices — Pizza With 3n Slices

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/pizza-with-3n-slices/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Given a circular pizza divided into 3n slices, select n non-adjacent slices such that the total sum of their sizes is maximized.

## 🔍 Key Observation

The problem is equivalent to selecting n/3 non-adjacent elements from a circular array of size 3n. Due to the circular property, the first and last elements cannot both be selected, breaking the problem into two linear DP subproblems: one excluding the last element and one excluding the first element.

## ⚙️ Algorithm

**Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n^2)` |

## 🏷️ Tags

`dynamic-programming` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def dp(self, slices: List[int], m: int) -> int:
        n = len(slices)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == 1:
                    dp[i][j] = slices[0]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + slices[i - 1])
        
        return dp[n][m]
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        return max(self.dp(slices[:-1], n // 3), self.dp(slices[1:], n // 3))
```

</details>
