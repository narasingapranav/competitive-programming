# 🟠 decode-ways — Decode Ways

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/decode-ways/) &nbsp;|&nbsp; **Solved:** 2026-07-10

---

## 📝 Summary

Accepted solution for Decode Ways on LeetCode.

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
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            one = int(s[i - 1])
            two = int(s[i - 2:i])
            if 1 <= one <= 9:
                dp[i] += dp[i - 1]
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]
        return dp[n]
```

</details>
