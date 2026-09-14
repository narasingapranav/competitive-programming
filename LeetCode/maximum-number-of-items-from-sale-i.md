# 🟠 maximum-number-of-items-from-sale-i — Maximum Number of Items From Sale I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-number-of-items-from-sale-i/) &nbsp;|&nbsp; **Solved:** 2026-05-31

---

## 📝 Summary

Accepted solution for Maximum Number of Items From Sale I on LeetCode.

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
    def maximumSaleItems(self, items, budget):
        n = len(items)

        bonus = [0] * n
        for i in range(n):
            f = items[i][0]
            cnt = 0
            for j in range(n):
                if items[j][0] % f == 0:
                    cnt += 1
            bonus[i] = cnt

        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + bonus[i])

        ans = 0

        for b in range(budget + 1):
            remaining = budget - b

            cheapest = min(x[1] for x in items)

            ans = max(ans, dp[b] + remaining // cheapest)

        return ans
```

</details>
