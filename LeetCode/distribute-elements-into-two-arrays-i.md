# 🟠 distribute-elements-into-two-arrays-i — Distribute Elements Into Two Arrays I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/distribute-elements-into-two-arrays-i/) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Accepted solution for Distribute Elements Into Two Arrays I on LeetCode.

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
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[nums[0]]
        arr2=[nums[1]]
        n=len(nums)
        i=2
        while i<n:
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
            i+=1
        return arr1+arr2
```

</details>
