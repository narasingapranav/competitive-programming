# 🟠 next-greater-element-iii — Next Greater Element III

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/next-greater-element-iii/) &nbsp;|&nbsp; **Solved:** 2026-08-13

---

## 📝 Summary

Given a positive 32-bit integer n, find the smallest integer greater than n that has the exact same digits. If no such integer exists or if the result overflows a 32-bit signed integer, return -1.

## 🔍 Key Observation

The problem is equivalent to finding the next lexicographical permutation of the digit sequence of n.

## ⚙️ Algorithm

**Next Permutation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(d)` | `O(d)` |

## 🏷️ Tags

`math` `two-pointers` `permutation` `string`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums=[]
        for i in str(n):
            nums.append(int(i))
        n=len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            return -1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])
        ans = int("".join(map(str, nums)))
        if ans > 2**31 - 1:
            return -1
        return ans
```

</details>
