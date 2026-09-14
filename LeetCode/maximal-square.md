# 🟠 maximal-square — Maximal Square

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximal-square/) &nbsp;|&nbsp; **Solved:** 2026-07-10

---

## 📝 Summary

Accepted solution for Maximal Square on LeetCode.

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
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        mx=0
        dp=[[0]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=int(matrix[i][j])
                    if dp[i][j]>mx:
                        mx=dp[i][j]
                elif matrix[i][j]=="0":
                    dp[i][j]=0
                else:
                    dp[i][j]=1+ min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    if dp[i][j]>mx:
                        mx=dp[i][j]
        return mx*mx
```

</details>
