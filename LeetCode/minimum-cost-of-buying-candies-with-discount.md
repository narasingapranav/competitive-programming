# 🟠 minimum-cost-of-buying-candies-with-discount — Minimum Cost of Buying Candies With Discount

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/) &nbsp;|&nbsp; **Solved:** 2026-06-01

---

## 📝 Summary

Accepted solution for Minimum Cost of Buying Candies With Discount on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        l = len(cost)
        for i in range(0, l, 3):
            total += cost[i]
            if i + 1 < l:
                total += cost[i + 1]
        return total
```

</details>
