# 🟠 longest-arithmetic-subsequence — Longest Arithmetic Subsequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-arithmetic-subsequence/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Find the length of the longest arithmetic subsequence in a given array of integers.

## 🔍 Key Observation

The longest arithmetic sequence ending at index i with a common difference d can be derived by adding 1 to the length of the sequence ending at index j (where j < i) with the exact same difference d.

## ⚙️ Algorithm

**Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n^2)` |

## 🏷️ Tags

`dynamic-programming` `hash-table` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[dict() for _ in range(n)]
        res=0
        for i in range(n):
            for j in range(i):
                d=nums[i]-nums[j]
                c=dp[j].get(d,1)+1
                dp[i][d]=c
                res=max(res,c)
        return res
```

</details>
