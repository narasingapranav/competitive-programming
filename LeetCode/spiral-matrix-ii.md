# 🟠 spiral-matrix-ii — Spiral Matrix II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/spiral-matrix-ii/) &nbsp;|&nbsp; **Solved:** 2026-05-27

---

## 📝 Summary

Accepted solution for Spiral Matrix II on LeetCode.

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
    def generateMatrix(self, n: int) -> List[List[int]]:
        x, y, dx, dy = 0, 0, 1, 0
        res = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n * n):
            res[y][x] = i + 1

            if not 0 <= x + dx < n or not 0 <= y + dy < n or res[y+dy][x+dx] != 0:
                dx, dy = -dy, dx
            
            x += dx
            y += dy

        return res
```

</details>
