# 🟠 sum-of-squares-of-special-elements — Sum of Squares of Special Elements 

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sum-of-squares-of-special-elements/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Calculate the sum of squares of elements in an array whose 1-based index evenly divides the total length of the array.

## 🔍 Key Observation

An element at 0-based index i is special if n is divisible by i + 1, which can be checked directly in a single pass.

## ⚙️ Algorithm

**Linear scan**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`array` `math`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int sumOfSquares(int[] nums) {
        int res=0;
        int n=nums.length;
        for (int i=0;i<n;i++){
            if ((n%(i+1))==0){
                res+=nums[i]*nums[i];
            }
        }
        return res;
    }
}
```

</details>
