# 🟠 minimum-common-value — Minimum Common Value

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-common-value/) &nbsp;|&nbsp; **Solved:** 2025-12-12

---

## 📝 Summary

Accepted solution for Minimum Common Value on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s=set(nums1)
        mi=None
        for i in nums2:
            if i in s:
                if mi is None or i < mi:
                    mi=i
        return mi if mi is not None else -1
```

</details>
