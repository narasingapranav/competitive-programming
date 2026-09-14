# 🟠 sudoku-solver — Sudoku Solver

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sudoku-solver/) &nbsp;|&nbsp; **Solved:** 2026-05-16

---

## 📝 Summary

Accepted solution for Sudoku Solver on LeetCode.

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
    def solveSudoku(self, board: list[list[str]]) -> None:
        n, N = 3, 9
        rows = [[0] * (N + 1) for _ in range(N)]
        cols = [[0] * (N + 1) for _ in range(N)]
        boxes = [[0] * (N + 1) for _ in range(N)]
        sudokuSolved = False

        def couldPlace(d, row, col):
            idx = (row // n) * n + col // n
            return rows[row][d] + cols[col][d] + boxes[idx][d] == 0

        def placeNumber(d, row, col):
            idx = (row // n) * n + col // n
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[idx][d] += 1
            board[row][col] = str(d)

        def removeNumber(d, row, col):
            idx = (row // n) * n + col // n
            rows[row][d] -= 1
            cols[col][d] -= 1
            boxes[idx][d] -= 1
            board[row][col] = '.'

        def placeNextNumbers(row, col):
            nonlocal sudokuSolved
            if row == N - 1 and col == N - 1:
                sudokuSolved = True
            elif col == N - 1:
                backtrack(row + 1, 0)
            else:
                backtrack(row, col + 1)

        def backtrack(row, col):
            nonlocal sudokuSolved
            if board[row][col] == '.':
                for d in range(1, 10):
                    if couldPlace(d, row, col):
                        placeNumber(d, row, col)
                        placeNextNumbers(row, col)
                        if not sudokuSolved:
                            removeNumber(d, row, col)
            else:
                placeNextNumbers(row, col)

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    placeNumber(int(board[i][j]), i, j)
        backtrack(0, 0)
```

</details>
