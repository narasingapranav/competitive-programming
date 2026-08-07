# 🟠 make-sum-divisible-by-p — Make Sum Divisible by P

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/make-sum-divisible-by-p/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Find the minimum length of a contiguous subarray to remove from an array such that the sum of the remaining elements is divisible by p.

## 🔍 Key Observation

The total array sum's remainder modulo p must equal the removed subarray's sum modulo p; we can track prefix sum remainders in a hash map to find the shortest such subarray.

## ⚙️ Algorithm

**Prefix sum + Hash map**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`array` `hash-table` `prefix-sum` `math`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totalrem=sum(nums)%p
        if totalrem==0:
            return 0
        ps=[0]*len(nums)
        ps[0]=nums[0]%p
        for i in range(1,len(nums)):
            ps[i]=(ps[i-1]+nums[i])%p
        m=len(nums)
        d={0:-1}
        for i in range(len(ps)):
            cr=ps[i]
            pr=(cr-totalrem+p)%p
            if pr in d:
                m=min(m,i-d[pr])
            d[cr]=i
        return -1 if m==len(nums) else m


```

</details>
