# 🟠 separate-squares-i — Separate Squares I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/separate-squares-i/) &nbsp;|&nbsp; **Solved:** 2026-01-14

---

## 📝 Summary

Accepted solution for Separate Squares I on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        total_area = 0
        low = float('inf')
        high = float('-inf')
        for x, y, l in squares:
            total_area += l * l
            low = min(low, y)
            high = max(high, y + l)
        half = total_area / 2
        def area_below(Y):
            area = 0
            for x, y, l in squares:
                if Y <= y:
                    continue
                elif Y >= y + l:
                    area += l * l
                else:
                    area += (Y - y) * l
            return area
        for _ in range(60):  
            mid = (low + high) / 2
            if area_below(mid) < half:
                low = mid
            else:
                high = mid
        return low
```

</details>
