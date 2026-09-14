# 🟠 remove-duplicates-from-sorted-array-ii — Remove Duplicates from Sorted Array II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) &nbsp;|&nbsp; **Solved:** 2026-09-09

---

## 📝 Summary

Accepted solution for Remove Duplicates from Sorted Array II on LeetCode.

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
    def removeDuplicates(self, nums: List[int]) -> int:
        c=Counter(nums)
        l=[]
        for i in c:
            if c[i]<=2:
                l.extend([i]*c[i])
            else:
                l.extend([i]*2)
        for i in range(len(l)):
            nums[i]=l[i]
        return len(l)
```

</details>
