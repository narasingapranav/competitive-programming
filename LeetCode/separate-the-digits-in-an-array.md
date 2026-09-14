# 🟠 separate-the-digits-in-an-array — Separate the Digits in an Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/separate-the-digits-in-an-array/) &nbsp;|&nbsp; **Solved:** 2026-05-11

---

## 📝 Summary

Accepted solution for Separate the Digits in an Array on LeetCode.

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
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if i<9:
                res.append(i)
            else:
                s=str(i)
                for j in s:
                    res.append(int(j))
        return res
```

</details>
