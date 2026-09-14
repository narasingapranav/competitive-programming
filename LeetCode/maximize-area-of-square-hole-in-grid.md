# 🟠 maximize-area-of-square-hole-in-grid — Maximize Area of Square Hole in Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/) &nbsp;|&nbsp; **Solved:** 2026-01-15

---

## 📝 Summary

Accepted solution for Maximize Area of Square Hole in Grid on LeetCode.

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
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        def longest(arr):
            arr.sort()
            best = cur = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    cur += 1
                else:
                    cur = 1
                best = max(best, cur)
            return best
        h = longest(hBars)
        v = longest(vBars)
        side = min(h, v) + 1
        return side * side
```

</details>
