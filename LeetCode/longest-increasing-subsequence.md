# 🟠 longest-increasing-subsequence — Longest Increasing Subsequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Find the length of the longest strictly increasing subsequence in a given integer array.

## 🔍 Key Observation

Maintaining an array of the smallest ending elements for all increasing subsequences of each length allows using binary search to greedily update or extend candidates in O(log n) time per element.

## ⚙️ Algorithm

**Binary search + greedy (Patience sorting)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`dynamic-programming` `binary-search` `lis` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bs(dp,n,target):
            l=0
            h=n
            while l<h:
                m=(l+h)//2
                if dp[m]>=target:
                    h=m
                else:
                    l=m+1
            return l
        n=len(nums)
        dp=[0]*(n)
        dp[0]=nums[0]
        size=1
        for i in range(1,n):
            lb=bs(dp,size,nums[i])
            if lb==size:
                size+=1
            dp[lb]=nums[i]
        return size
```

</details>
