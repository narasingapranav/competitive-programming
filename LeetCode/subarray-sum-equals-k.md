# 🟠 subarray-sum-equals-k — Subarray Sum Equals K

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Find the total number of contiguous subarrays within an array whose sum equals a given target integer k.

## 🔍 Key Observation

The sum of any subarray starting at index i and ending at index j can be computed incrementally by accumulating elements in an inner loop.

## ⚙️ Algorithm

**Brute force iteration**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(1)` |

## 🏷️ Tags

`array` `prefix-sum` `brute-force`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int c=0;
        for(int i=0;i<nums.length;i++){
            int s=0;
            for(int j=i;j<nums.length;j++){
                s+=nums[j];
                if(s==k){
                    c++;
                }
            }
        }
        return c;
    }
}
```

</details>
