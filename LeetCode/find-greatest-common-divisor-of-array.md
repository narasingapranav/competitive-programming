# 🟠 find-greatest-common-divisor-of-array — Find Greatest Common Divisor of Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) &nbsp;|&nbsp; **Solved:** 2025-10-11

---

## 📝 Summary

Accepted solution for Find Greatest Common Divisor of Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        return math.gcd(mini,maxi)
```

</details>
