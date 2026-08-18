# 🟠 perfect-squares — Perfect Squares

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/perfect-squares/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Find the minimum number of perfect square numbers that sum to a given integer n.

## 🔍 Key Observation

The problem can be modeled as a variant of the unbounded knapsack / coin change problem where the allowed item values are perfect squares up to n.

## ⚙️ Algorithm

**Dynamic Programming (Top-down with Memoization)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * sqrt(n))` | `O(n)` |

## 🏷️ Tags

`dynamic-programming` `memoization` `math`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numSquares(self, n: int) -> int:
        def ps(sq,n,memo):
            if memo[n] !=-1:
                return memo[n]
            if n==0:
                return 0
            mx=n+1
            for i in sq:
                if i<=n:
                    mx=min(mx,1+ps(sq,n-i,memo))
            memo[n]=mx
            return mx
        sq=[]
        i=1
        memo=[-1]*(n+1)
        while i*i<=n:
            sq.append(i*i)
            i+=1
        return ps(sq,n,memo)
```

</details>
