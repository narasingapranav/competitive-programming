# 🟠 maximum-k-to-sort-a-permutation — Maximum K to Sort a Permutation

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-k-to-sort-a-permutation/) &nbsp;|&nbsp; **Solved:** 2025-08-15

---

## 📝 Summary

Accepted solution for Maximum K to Sort a Permutation on LeetCode.

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
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pow2 = 1
        while pow2 < n:
            pow2 <<= 1
        max_k = pow2 - 1
        
        k = max_k
        for i, val in enumerate(nums):
            if val != i:
                k &= val
        
        return 0 if k == max_k else k
```

</details>
