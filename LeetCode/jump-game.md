# 🟠 jump-game — Jump Game

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/jump-game/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Accepted solution for Jump Game on LeetCode.

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
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[False]*(n)
        dp[-1]=True
        for i in range(n-2,-1,-1):
            far=min(i+nums[i],n-1)
            for j in range(i+1,far+1):
                if dp[j]:
                    dp[i]=True
                    break
        return dp[0]
```

</details>
