# 🟠 minimum-lines-to-represent-a-line-chart — Minimum Lines to Represent a Line Chart

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Accepted solution for Minimum Lines to Represent a Line Chart on LeetCode.

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
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n <= 1:
            return 0
        stockPrices.sort()
        count = 1
        x1, y1 = stockPrices[0]
        x2, y2 = stockPrices[1]
        dx_prev = x2 - x1
        dy_prev = y2 - y1
        for i in range(2, n):
            x3, y3 = stockPrices[i]
            dx = x3 - x2
            dy = y3 - y2
            if dy * dx_prev != dy_prev * dx:
                count += 1
            dx_prev = dx
            dy_prev = dy
            x2, y2 = x3, y3
        return count
```

</details>
