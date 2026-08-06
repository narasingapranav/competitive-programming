# 🟠 number-of-1-bits — Number of 1 Bits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-1-bits/) &nbsp;|&nbsp; **Solved:** 2026-08-06

---

## 📝 Summary

Given an unsigned integer, count and return the number of set bits ('1's) in its binary representation.

## 🔍 Key Observation

The least significant bit can be isolated using the bitwise AND operator (`n & 1`), and shifting right by one bit (`n >>= 1`) processes each bit sequentially until the number becomes zero.

## ⚙️ Algorithm

**Bit manipulation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`bit-manipulation` `bitwise`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n:
            c+=n&1
            n>>=1
        return c
```

</details>
