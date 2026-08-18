# 🟠 integer-break — Integer Break

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/integer-break/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Given a positive integer n, break it into the sum of at least two positive integers such that the product of those integers is maximized.

## 🔍 Key Observation

To maximize the product, the sum should be decomposed into as many 3s as possible; a remainder of 1 is combined with a 3 to form 2 * 2 = 4, and a remainder of 2 is multiplied as a 2.

## ⚙️ Algorithm

**Math / Greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n)` | `O(1)` |

## 🏷️ Tags

`math` `greedy` `dynamic-programming`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2: return 1
        if n==3: return 2
        q=n//3
        r=n%3
        return 3**q if r==0 else 3**(q-1) * 4 if r==1 else (3**q) * 2

```

</details>
