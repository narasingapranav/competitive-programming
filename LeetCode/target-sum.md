# 🟠 target-sum — Target Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/target-sum/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Given an array of integers and a target value, count the number of ways to assign '+' or '-' signs to each integer such that the total sum equals the target.

## 🔍 Key Observation

The problem can be re-framed as finding the number of subsets with sum P such that 2 * P = sum(nums) + target, transforming it into a standard 0/1 Knapsack (Subset Sum) problem.

## ⚙️ Algorithm

**Dynamic Programming (Subset Sum)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * T)` | `O(T)` |

## 🏷️ Tags

`dynamic-programming` `subset-sum` `knapsack` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # p = set of positive numbers
        # n = set of negative numbers
        # sum of p + sum of n = sum of nums
        # sum of p - sum of n = target
        # 2*sum of p          = target + sum of nums
        # sum of p            = (target + sum of nums)//2
        s=sum(nums)
        if abs(target)>s: return 0
        if (s+target)%2==1: return 0
        t=(s+target)//2
        dp=[0]*(t+1)
        dp[0]=1
        for i in nums:
            for j in range(t,i-1,-1):
                dp[j]+=dp[j-i]
        return dp[t]
```

</details>
