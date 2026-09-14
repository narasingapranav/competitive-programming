# 🟠 split-array-largest-sum — Split Array Largest Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/split-array-largest-sum/) &nbsp;|&nbsp; **Solved:** 2026-02-25

---

## 📝 Summary

Accepted solution for Split Array Largest Sum on LeetCode.

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
    def splitArray(self, nums: List[int], k: int) -> int:
        def func(nums,mid):
            a=1
            s=0
            for i in range(len(nums)):
                if s+nums[i]<=mid:
                    s+=nums[i]
                else:
                    a+=1
                    s=nums[i]
            return a
        if len(nums)==k:
            return max(nums)
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid= low+ (high-low)//2
            splits=func(nums,mid)
            if splits<=k:
                high=mid-1
            else:
                low=mid+1
        return low
```

</details>
