# 🟠 special-positions-in-a-binary-matrix — Special Positions in a Binary Matrix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/special-positions-in-a-binary-matrix/) &nbsp;|&nbsp; **Solved:** 2026-03-04

---

## 📝 Summary

Accepted solution for Special Positions in a Binary Matrix on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        rows=[0]*n
        cols=[0]*m
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    rows[i]+=1
                    cols[j]+=1
        count=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1 and rows[i]==1 and cols[j]==1:
                    count+=1
        return count
```

</details>
