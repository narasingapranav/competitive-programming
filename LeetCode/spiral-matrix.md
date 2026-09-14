# 🟠 spiral-matrix — Spiral Matrix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/spiral-matrix/) &nbsp;|&nbsp; **Solved:** 2025-10-11

---

## 📝 Summary

Accepted solution for Spiral Matrix on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^5) (estimated -- 5 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a=[]
        t,b,l,r=0,len(matrix)-1,0,len(matrix[0])-1
        while l<=r and t<=b:
            for i in range(l,r+1):
                a.append(matrix[t][i])
            t+=1
            for i in range(t,b+1):
                a.append(matrix[i][r])
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    a.append(matrix[b][i])
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    a.append(matrix[i][l])
                l+=1
        return a
```

</details>
