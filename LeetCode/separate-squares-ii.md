# 🟠 separate-squares-ii — Separate Squares II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/separate-squares-ii/) &nbsp;|&nbsp; **Solved:** 2026-01-14

---

## 📝 Summary

Accepted solution for Separate Squares II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()
        xs = []
        prev_y = events[0][0]
        total = 0
        areas = []

        def union_len(intervals):
            intervals.sort()
            res = cur = 0
            end = -10**30
            for a, b in intervals:
                if a > end:
                    res += b - a
                    end = b
                elif b > end:
                    res += b - end
                    end = b
            return res

        for y, typ, x1, x2 in events:
            if y > prev_y and xs:
                h = y - prev_y
                w = union_len(xs)
                areas.append((prev_y, h, w))
                total += h * w
            if typ == 1:
                xs.append((x1, x2))
            else:
                xs.remove((x1, x2))
            prev_y = y

        half = total / 2
        acc = 0
        for y, h, w in areas:
            if acc + h * w >= half:
                return y + (half - acc) / w
            acc += h * w

        return 0.0
```

</details>
