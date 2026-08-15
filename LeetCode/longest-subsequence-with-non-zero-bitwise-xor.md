# 🟠 longest-subsequence-with-non-zero-bitwise-xor — Longest Subsequence With Non-Zero Bitwise XOR

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Find the length of the longest subsequence of an array whose elements have a non-zero bitwise XOR sum.

## 🔍 Key Observation

If the bitwise XOR sum of all elements is non-zero, the whole array works; if it is zero and at least one non-zero element exists, removing one non-zero element gives a non-zero XOR sum of length n - 1; if all elements are zero, no such subsequence exists.

## ⚙️ Algorithm

**Greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`array` `bit-manipulation` `greedy`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        tot = nz = 0

        for n in nums:
            nz |= n > 0
            tot ^= n

        return nz * (len(nums) - (not tot))
```

</details>
