# 🟠 longest-arithmetic-subsequence — Longest Arithmetic Subsequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-arithmetic-subsequence/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Accepted solution for Longest Arithmetic Subsequence on LeetCode.

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
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[defaultdict() for _ in range(n)]
        res=0
        for i in range(n):
            for j in range(i):
                d=nums[i]-nums[j]
                c=dp[j].get(d,1)+1
                dp[i][d]=c
                res=max(res,c)
        return res
```

</details>
