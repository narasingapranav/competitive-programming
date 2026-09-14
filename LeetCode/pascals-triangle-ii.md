# 🟠 pascals-triangle-ii — Pascal's Triangle II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/pascals-triangle-ii/) &nbsp;|&nbsp; **Solved:** 2025-12-03

---

## 📝 Summary

Accepted solution for Pascal's Triangle II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]*(rowIndex+1)
        for i in range(1,rowIndex):
            for j in range(i,0,-1):
                row[j]+=row[j-1]
        return row
```

</details>
