# 🟠 search-a-2d-matrix — Search a 2D Matrix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/search-a-2d-matrix/) &nbsp;|&nbsp; **Solved:** 2026-07-01

---

## 📝 Summary

Accepted solution for Search a 2D Matrix on LeetCode.

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
import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix=np.array(matrix)
        a=matrix.flatten()
        l,h=0,len(a)-1
        while l<=h:
            m=l+((h-l)//2)
            if a[m]==target: return True
            if a[m]<target: l=m+1
            else: h=m-1
        return False
```

</details>
