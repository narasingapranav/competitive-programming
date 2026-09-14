# 🟠 set-matrix-zeroes — Set Matrix Zeroes

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/set-matrix-zeroes/) &nbsp;|&nbsp; **Solved:** 2026-05-01

---

## 📝 Summary

Accepted solution for Set Matrix Zeroes on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^9) (estimated -- 9 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''z=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    z.append([i,j])
        n=len(matrix)
        m=len(matrix[0])
        for c in z:
            for i in range(n):
                for j in range(m):
                    if i==c[0] or j==c[1]:
                        matrix[i][j]=0'''
        c=set()
        r=set()
        n,m=len(matrix),len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)
        for i in range(n):
            for j in range(m):
                if i in r or j in c:
                    matrix[i][j]=0
```

</details>
