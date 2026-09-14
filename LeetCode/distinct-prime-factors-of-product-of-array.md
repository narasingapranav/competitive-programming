# 🟠 distinct-prime-factors-of-product-of-array — Distinct Prime Factors of Product of Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/) &nbsp;|&nbsp; **Solved:** 2026-02-23

---

## 📝 Summary

Accepted solution for Distinct Prime Factors of Product of Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        result = set()
        for num in nums:
            factor = 2
            while factor * factor <= num:
                while num % factor == 0:
                    result.add(factor)
                    num //= factor
                factor += 1
            if num > 1:
                result.add(num)
        return len(result)
```

</details>
