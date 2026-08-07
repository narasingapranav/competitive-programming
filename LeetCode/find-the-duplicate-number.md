# 🟠 find-the-duplicate-number — Find the Duplicate Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Given an array of integers containing n + 1 numbers in the range [1, n], find and return the duplicate number.

## 🔍 Key Observation

Iterating through the array while storing seen elements in a hash set allows immediate detection of the duplicate when an element is encountered a second time.

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
    public int findDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int i:nums){
            if (set.contains(i)) return i;
            set.add(i);
        }
        return 0;
    }
}
```

</details>
