# 🟠 delete-and-earn — Delete and Earn

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/delete-and-earn/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Given an array of integers, maximize points by repeatedly picking an element to earn its value while deleting all occurrences of that value plus or minus one.

## 🔍 Key Observation

Aggregating total points by value transforms the problem into a variation of the House Robber problem, where picking value i prevents taking value i-1.

## ⚙️ Algorithm

**Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N + M)` | `O(M)` |

## 🏷️ Tags

`dynamic-programming` `array` `hash-table`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq=Counter(nums)
        m=max(nums)
        dp=[0]*(m+1)
        dp[0]=0
        dp[1]=freq[1]*1
        for i in range(2,m+1):
            dp[i]=max(dp[i-1],freq[i]*i+dp[i-2])
        return dp[m]
```

</details>
