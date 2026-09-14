# 🟠 n-th-tribonacci-number — N-th Tribonacci Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/n-th-tribonacci-number/) &nbsp;|&nbsp; **Solved:** 2026-05-14

---

## 📝 Summary

Accepted solution for N-th Tribonacci Number on LeetCode.

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
    def tribonacci(self, n: int) -> int:
        dp=[-1]*(n+1)
        dp[0]=0
        if n>=1:
            dp[1]=1
        if n>=2:
            dp[2]=1
        if n>=3:
            dp[3]=2
        for i in range(4,n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]
```

</details>
