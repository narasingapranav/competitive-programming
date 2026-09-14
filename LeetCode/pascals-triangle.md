# 🟠 pascals-triangle — Pascal's Triangle

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/pascals-triangle/) &nbsp;|&nbsp; **Solved:** 2025-08-16

---

## 📝 Summary

Accepted solution for Pascal's Triangle on LeetCode.

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
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for _ in range(1, numRows):
            triangle.append([1] + [triangle[-1][i] + triangle[-1][i+1] for i in range(len(triangle[-1])-1)] + [1])
        return triangle
```

</details>
