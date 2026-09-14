# 🟠 find-target-indices-after-sorting-array — Find Target Indices After Sorting Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-target-indices-after-sorting-array/) &nbsp;|&nbsp; **Solved:** 2025-12-11

---

## 📝 Summary

Accepted solution for Find Target Indices After Sorting Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Two pointers**

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
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def quick(arr):
            if len(arr)<=1:
                return arr
            p=arr[len(arr)//2]
            left=[i for i in arr if i<p]
            middle=[i for i in arr if i==p]
            right=[i for i in arr if i>p]
            return quick(left)+middle+quick(right)

        a=quick(nums)
        ind=[]
        for i in range(len(a)):
            if a[i]==target:
                ind.append(i)
        return ind
```

</details>
