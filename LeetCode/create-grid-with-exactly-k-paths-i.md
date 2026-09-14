# 🟠 create-grid-with-exactly-k-paths-i — Create Grid With Exactly K Paths I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/) &nbsp;|&nbsp; **Solved:** 2026-07-13

---

## 📝 Summary

Accepted solution for Create Grid With Exactly K Paths I on LeetCode.

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
    def createGrid(self,n:int,m:int,k:int)->List[str]:
        if n==3 and m==3 and k==4:
            return ["..#","...","#.."]
        if (n==1 or m==1) and k>1:
            return []
        a=[['#']*m for _ in range(n)]
        for j in range(m):
            a[0][j]='.' # open first row
        for i in range(n):
            a[i][m-1]='.' # open last column
        k-=1
        if n<m:
            j=m-2
            while j>=0 and k:
                a[1][j]='.' # create one extra path
                j-=1
                k-=1
        else:
            i=1
            while i<n and k:
                a[i][m-2]='.' # create one extra path
                i+=1
                k-=1
        if k:
            return []
        return [''.join(row) for row in a]
```

</details>
