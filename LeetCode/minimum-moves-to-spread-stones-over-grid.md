# 🟠 minimum-moves-to-spread-stones-over-grid — Minimum Moves to Spread Stones Over Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Given a 3x3 grid containing 9 total stones, find the minimum number of moves (Manhattan distance) required to redistribute the stones so that every cell has exactly one stone.

## 🔍 Key Observation

Because the grid is strictly 3x3, there are at most 8 empty cells, making a full search (backtracking) over all pairings of extra stones to empty cells computationally trivial.

## ⚙️ Algorithm

**Backtracking**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(S!)` | `O(S)` |

## 🏷️ Tags

`backtracking` `recursion` `grid` `brute-force`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        need, has = [], {}
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    need.append((i, j))
                if grid[i][j] > 1:
                    has[(i, j)] = grid[i][j]
        
        def go():
            if len(need) == 0: return 0
            best = inf
            i1, j1 = need.pop()
            for (i2, j2) in has.keys():
                if has[(i2, j2)] == 1:
                    continue
                has[(i2, j2)] -= 1
                cost = abs(i2 - i1) + abs(j2 - j1)
                best = min(best, go() + cost)
                has[(i2, j2)] += 1
            need.append((i1, j1))
            return best

        return go()
```

</details>
