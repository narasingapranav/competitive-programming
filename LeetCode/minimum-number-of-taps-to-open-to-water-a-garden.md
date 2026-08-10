# 🟠 minimum-number-of-taps-to-open-to-water-a-garden — Minimum Number of Taps to Open to Water a Garden

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Determine the minimum number of taps needed to water a 1D garden of length n, where each tap can water a specific continuous interval around its position.

## 🔍 Key Observation

Converting each tap into an interval [start, end] allows updating the minimum taps needed to cover up to point j in (start, end] using the value at dp[start].

## ⚙️ Algorithm

**Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * R)` | `O(n)` |

## 🏷️ Tags

`dynamic-programming` `greedy` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i, r in enumerate(ranges):
            start, end = max(0, i - r), min(n, i + r)
            for j in range(start + 1, end + 1):
                dp[j] = min(dp[j], dp[start] + 1)
                
        return dp[-1] if dp[-1] != float('inf') else -1
```

</details>
