# 🟠 first-missing-positive — First Missing Positive

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/first-missing-positive/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Find the smallest missing positive integer from an unsorted array of integers.

## 🔍 Key Observation

The smallest missing positive integer must fall within the range [1, n + 1], where n is the length of the array.

## ⚙️ Algorithm

**Hash Set Lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`array` `hash-table`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int firstMissingPositive(int[] nums) {
      int n=nums.length;
      HashSet<Integer> set = new HashSet<>();
      for(int i:nums){
        set.add(i);
      }
      for(int i=1;i<=n+1;i++){
        if(!set.contains(i)){
            return i;
        }
      }  
      return 0;
    }
}
```

</details>
