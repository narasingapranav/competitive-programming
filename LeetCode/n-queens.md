# 🟠 n-queens — N-Queens

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/n-queens/) &nbsp;|&nbsp; **Solved:** 2025-08-16

---

## 📝 Summary

Accepted solution for N-Queens on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, diagonals, anti_diagonals, cols, state):
            if row == n:
                board = [''.join(r) for r in state]
                result.append(board)
                return
            for col in range(n):
                curr_diag = row - col
                curr_anti_diag = row + col
                if (col in cols or
                    curr_diag in diagonals or
                    curr_anti_diag in anti_diagonals):
                    continue
                state[row][col] = 'Q'
                cols.add(col)
                diagonals.add(curr_diag)
                anti_diagonals.add(curr_anti_diag)

                backtrack(row + 1, diagonals, anti_diagonals, cols, state)
                state[row][col] = '.'
                cols.remove(col)
                diagonals.remove(curr_diag)
                anti_diagonals.remove(curr_anti_diag)

        result = []
        empty_board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return result

```

</details>
