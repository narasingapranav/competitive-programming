# 🟠 rotate-array — Rotate Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-cpp-00599C?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rotate-array/) &nbsp;|&nbsp; **Solved:** 2026-08-12

---

## 📝 Summary

Given an array of integers, rotate the array to the right by k steps in-place.

## 🔍 Key Observation

Reversing the entire array, followed by reversing the first k elements and then the remaining n-k elements, achieves the right-rotation in-place.

## ⚙️ Algorithm

**Three-step reversal**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`array` `two-pointers` `math` `in-place`

<details>
<summary>💻 View solution</summary>

```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n=nums.size();
        k%=n;
        reverse(nums.begin(),nums.end());
        reverse(nums.begin(),nums.begin()+k);
        reverse(nums.begin()+k,nums.end());
    }
};
```

</details>
