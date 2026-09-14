# 🟠 maximum-product-of-three-numbers — Maximum Product of Three Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers/) &nbsp;|&nbsp; **Solved:** 2026-05-05

---

## 📝 Summary

Accepted solution for Maximum Product of Three Numbers on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        s1=nums[0]*nums[1]*nums[-1]
        s2=nums[-1]*nums[-2]*nums[-3]
        return max(s1,s2)
```

</details>
