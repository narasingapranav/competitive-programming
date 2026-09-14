# 🟠 reshape-the-matrix — Reshape the Matrix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reshape-the-matrix/) &nbsp;|&nbsp; **Solved:** 2026-08-29

---

## 📝 Summary

Accepted solution for Reshape the Matrix on LeetCode.

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
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flattened=[j for i in mat for j in i]
        res=[]
        if len(flattened) != r * c:
            return mat
        res = []
        for i in range(0, len(flattened), c):
            res.append(flattened[i : i + c])
        return res
```

</details>
