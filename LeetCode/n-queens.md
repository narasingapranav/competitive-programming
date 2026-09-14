# 🟠 n-queens — N-Queens

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/n-queens/) &nbsp;|&nbsp; **Solved:** 2026-05-16

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
        board=[['.']*n for _ in range(n)]
        l=[]
        d=set()
        ad=set()
        co=set()
        def place(r,c):
            board[r][c]='Q'
        def remove(r,c):
            board[r][c]='.'
        def solve(r):
            if r==n:
                l.append(["".join(r) for r in board])
                return
            for c in range(n):
                if c in co or (r-c) in d or (r+c) in ad:
                    continue
                place(r,c)
                co.add(c)
                d.add(r-c)
                ad.add(r+c)
                solve(r+1)
                remove(r,c)
                co.remove(c)
                d.remove(r-c)
                ad.remove(r+c)
        solve(0)
        return l
```

</details>
