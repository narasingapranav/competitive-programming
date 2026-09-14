# 🟠 next-greater-element-i — Next Greater Element I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/next-greater-element-i/) &nbsp;|&nbsp; **Solved:** 2026-07-19

---

## 📝 Summary

Accepted solution for Next Greater Element I on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = [-1]*len(nums1)

        for i in range(len(nums1)):
            f = -1
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    f+=1
                if f == 0:
                    if nums1[i] < nums2[j]:
                        result[i]  = nums2[j]
                        break
        return result
```

</details>
