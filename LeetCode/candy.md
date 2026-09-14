# 🟠 candy — Candy

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/candy/) &nbsp;|&nbsp; **Solved:** 2026-07-10

---

## 📝 Summary

Accepted solution for Candy on LeetCode.

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
    def candy(self, rating: List[int]) -> int:
        n=len(rating)
        dp=[1]*n
        for i in range(1,n):
            if rating[i]>rating[i-1]:
                dp[i]=dp[i-1]+1
        for i in range(n-2,-1,-1):
            if rating[i+1]<rating[i]:
                dp[i]=max(dp[i],dp[i+1]+1)
        return sum(dp)
```

</details>
