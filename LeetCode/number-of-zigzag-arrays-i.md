# 🟠 number-of-zigzag-arrays-i — Number of ZigZag Arrays I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-i/) &nbsp;|&nbsp; **Solved:** 2026-06-23

---

## 📝 Summary

Accepted solution for Number of ZigZag Arrays I on LeetCode.

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
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        dp = [1] * m

        for i in range(2, n + 1):
            dp.reverse()
            s = 0
            for j in range(m):
                dp[j], s = s, (s + dp[j]) % MOD

        return (sum(dp) % MOD << 1) % MOD
```

</details>
