# 🟠 longest-subarray-with-at-most-k-distinct-prime-factors — Longest Subarray With at Most K Distinct Prime Factors

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-subarray-with-at-most-k-distinct-prime-factors/) &nbsp;|&nbsp; **Solved:** 2026-08-23

---

## 📝 Summary

Accepted solution for Longest Subarray With at Most K Distinct Prime Factors on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion + Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^5) (estimated -- 5 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`recursion` `hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findfactors(self,num):
        s=set()
        d=2
        while d*d<=num:
            while num%d==0:
                s.add(d)
                num//=d
            d+=1
        if num>1:
            s.add(num)
        return s
    def longestSubarray(self, nums: list[int], k: int) -> int:
        res=0
        l=0
        dict={}
        for r in range(len(nums)):
            for i in self.findfactors(nums[r]):
                dict[i]=dict.get(i,0)+1
            while len(dict)>k:
                for i in self.findfactors(nums[l]):
                    dict[i]-=1
                    if dict[i]==0:
                        del dict[i]
                l+=1
            res=max(res,r-l+1)
        return res
```

</details>
