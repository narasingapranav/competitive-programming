# 🟠 best-time-to-buy-and-sell-stock — Best Time to Buy and Sell Stock

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) &nbsp;|&nbsp; **Solved:** 2025-09-06

---

## 📝 Summary

Accepted solution for Best Time to Buy and Sell Stock on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mip=float('inf')
        maxpro=0
        for i in prices:
            mip=min(mip,i)
            p=i-mip
            maxpro=max(maxpro,p)
        return maxpro
```

</details>
