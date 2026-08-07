# 🟠 sum-of-square-numbers — Sum of Square Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sum-of-square-numbers/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Given a non-negative integer c, determine whether there exist two integers a and b such that a^2 + b^2 = c.

## 🔍 Key Observation

Since the search space for both integers is bounded between 0 and sqrt(c), we can treat the range as a sorted array and use two pointers to find if any pair sums to c.

## ⚙️ Algorithm

**Two Pointers**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(sqrt(c))` | `O(1)` |

## 🏷️ Tags

`math` `two-pointers`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public boolean judgeSquareSum(int c) {
        long l=0;
        long h=(int)Math.sqrt(c);
        while (l<=h){
            long ans=l*l + h*h;
            if (ans==c){
                return true;
            }
            else if (ans>c){
                h--;
            }
            else{
                l++;
            }
        }
        return false;
    }
}
```

</details>
