# 🟠 minimum-common-value — Minimum Common Value

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-common-value/) &nbsp;|&nbsp; **Solved:** 2026-05-19

---

## 📝 Summary

Accepted solution for Minimum Common Value on LeetCode.

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
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        answer = -1
        n = len(nums1)
        m = len(nums2)
        i, j = 0, 0
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                answer = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return answer
```

</details>
