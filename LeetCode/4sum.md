# 🟠 4sum — 4Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/4sum/) &nbsp;|&nbsp; **Solved:** 2025-12-06

---

## 📝 Summary

Accepted solution for 4Sum on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^5) (estimated -- 5 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        a=[]
        for i in range(n):
            if i >0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l,r=j+1,n-1
                while l<r:
                    t=nums[i]+nums[j]+nums[l]+nums[r]
                    if t==target:
                        a.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif t<target:
                        l+=1
                    else:
                        r-=1
        return a
```

</details>
