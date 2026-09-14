# 🟠 minimum-element-after-replacement-with-digit-sum — Minimum Element After Replacement With Digit Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/) &nbsp;|&nbsp; **Solved:** 2026-05-29

---

## 📝 Summary

Accepted solution for Minimum Element After Replacement With Digit Sum on LeetCode.

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
    def minElement(self, nums: List[int]) -> int:
        res = 36
        for n in nums:
            res = min(res, n - 9 * ((n//10) + (n//100) + (n//1000) + (n//10000)))
            
        return res
```

</details>
