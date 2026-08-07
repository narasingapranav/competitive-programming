# 🟠 maximum-product-subarray — Maximum Product Subarray

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-product-subarray/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Find the contiguous subarray within a given integer array that has the largest product and return that maximum product.

## 🔍 Key Observation

The product of any contiguous subarray starting at index i and ending at index j can be computed iteratively by multiplying the accumulated product by nums[j].

## ⚙️ Algorithm

**Brute force enumeration**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(1)` |

## 🏷️ Tags

`array` `math`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int maxProduct(int[] nums) {
        int m=0;
        if (nums.length==1) return nums[0];
        for(int i=0;i<nums.length;i++){
            int p=1;
            for (int j=i;j<nums.length;j++){
                p*=nums[j];
                m=Math.max(p,m);
            }
        }
        return m;
    }
}
```

</details>
