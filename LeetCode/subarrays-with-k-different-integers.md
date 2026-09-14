# 🟠 subarrays-with-k-different-integers — Subarrays with K Different Integers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/subarrays-with-k-different-integers/) &nbsp;|&nbsp; **Solved:** 2025-12-12

---

## 📝 Summary

Accepted solution for Subarrays with K Different Integers on LeetCode.

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
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            d={}
            i=0
            ans=0
            n=len(nums)
            for j in range(n):
                d[nums[j]]=d.get(nums[j],0)+1
                while len(d)>k:
                    d[nums[i]]-=1
                    if d[nums[i]]==0:
                        del d[nums[i]]
                    i+=1
                ans+=j-i+1
            return ans
        return atmost(k)-atmost(k-1)

```

</details>
