# 🟠 smallest-divisible-digit-product-i — Smallest Divisible Digit Product I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-i/) &nbsp;|&nbsp; **Solved:** 2026-08-06

---

## 📝 Summary

Find the smallest integer greater than or equal to n such that the product of its digits is divisible by t.

## 🔍 Key Observation

A valid number is guaranteed to be found within at most 10 increments because any number ending in 0 has a digit product of 0, which is divisible by any t.

## ⚙️ Algorithm

**Brute-force iteration**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n)` | `O(log n)` |

## 🏷️ Tags

`math` `brute-force` `digits`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def p(n):
            ans=1
            n=str(n)
            for i in n:
                ans*=int(i)
            return ans
        while p(n)%t!=0:
            n+=1
        return n
```

</details>
