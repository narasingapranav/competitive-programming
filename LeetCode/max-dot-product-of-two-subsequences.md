# 🟠 max-dot-product-of-two-subsequences — Max Dot Product of Two Subsequences

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) &nbsp;|&nbsp; **Solved:** 2026-01-09

---

## 📝 Summary

Accepted solution for Max Dot Product of Two Subsequences on LeetCode.

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
    def maxDotProduct(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        NEG_INF = -10**9

        dp = [[NEG_INF] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                prod = nums1[i] * nums2[j]
                dp[i][j] = max(
                    prod,
                    prod + dp[i + 1][j + 1],
                    dp[i + 1][j],
                    dp[i][j + 1]
                )

        return dp[0][0]
```

</details>
