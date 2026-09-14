# 🟠 median-of-two-sorted-arrays — Median of Two Sorted Arrays

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) &nbsp;|&nbsp; **Solved:** 2025-07-08

---

## 📝 Summary

Accepted solution for Median of Two Sorted Arrays on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        l1,l2=len(nums1),len(nums2)
        l,r=0,l1
        while l<=r:
            p1=(l+r)//2
            p2=(l1+l2+1)//2-p1
            max_l1=float('-inf') if p1==0 else nums1[p1-1]
            max_l2=float('-inf') if p2==0 else nums2[p2-1]
            min_r1=float('inf') if p1==l1 else nums1[p1]
            min_r2=float('inf') if p2==l2 else nums2[p2]
            if max_l1<=min_r2 and max_l2<=min_r1:
                if (l1+l2)%2==0:
                    return (max(max_l1,max_l2)+min(min_r1,min_r2))/2
                else:
                    return max(max_l1,max_l2)
            elif max_l1>min_r2:
                r=p1-1
            else:
                l=p1+1
        
```

</details>
