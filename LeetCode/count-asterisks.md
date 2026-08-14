# 🟠 count-asterisks — Count Asterisks

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-asterisks/) &nbsp;|&nbsp; **Solved:** 2026-08-13

---

## 📝 Summary

Count the total number of '*' characters in a string that do not lie between any pair of '|' delimiters.

## 🔍 Key Observation

Splitting the string by '|' places segments outside of vertical bars at even indices and segments inside vertical bars at odd indices.

## ⚙️ Algorithm

**String splitting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`string` `parsing`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countAsterisks(self, s: str) -> int:
        r=s.split('|')
        ans=0
        for i in range(0,len(r),2):
            ans+=r[i].count('*')
        return ans
```

</details>
