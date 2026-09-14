# 🟠 permutations-ii — Permutations II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/permutations-ii/) &nbsp;|&nbsp; **Solved:** 2025-12-09

---

## 📝 Summary

Accepted solution for Permutations II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l=permutations(nums)
        a=set()
        for i in l:
            a.add(tuple(i))
        b=[]
        for i in a:
            b.append(list(i))
        return b
```

</details>
