# 🟠 maximum-ice-cream-bars — Maximum Ice Cream Bars

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-ice-cream-bars/) &nbsp;|&nbsp; **Solved:** 2026-06-21

---

## 📝 Summary

Accepted solution for Maximum Ice Cream Bars on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)

        freq = [0] * (max_cost + 1)

        for cost in costs:
            freq[cost] += 1

        ans = 0

        for price in range(1, max_cost + 1):
            if freq[price] == 0:
                continue

            can_buy = min(freq[price], coins // price)

            ans += can_buy
            coins -= can_buy * price

            if coins < price:
                break

        return ans
```

</details>
