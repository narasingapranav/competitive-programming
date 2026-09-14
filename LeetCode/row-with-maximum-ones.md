# 🟠 row-with-maximum-ones — Row With Maximum Ones

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/row-with-maximum-ones/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Accepted solution for Row With Maximum Ones on LeetCode.

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
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ro=0
        mo=0
        mr=0
        for i in range(len(mat)):
            ro=sum(mat[i])
            if ro>mo:
                mr=i
                mo=ro
        return [mr,mo]
```

</details>
