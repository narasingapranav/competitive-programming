# 🟠 n-queens — N-Queens

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/n-queens/) &nbsp;|&nbsp; **Solved:** 2026-05-16

---

## 📝 Summary

Accepted solution for N-Queens on LeetCode.

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
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)]
        l=[]
        def issafe(r,c,b):
            for i in range(n):
                for j in range(n):
                    if b[i][j]=='Q':
                        if abs(r-i)==abs(c-j) or r==i or c==j:
                            return False
            return True
        def place(r,c):
            board[r][c]='Q'
        def remove(r,c):
            board[r][c]='.'
        def solve(r):
            if r==n:
                l.append(["".join(r) for r in board])
            for c in range(n):
                if issafe(r,c,board):
                    place(r,c)
                    solve(r+1)
                    remove(r,c)
        solve(0)
        return l
```

</details>
