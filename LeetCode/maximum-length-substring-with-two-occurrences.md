# 🟠 maximum-length-substring-with-two-occurrences — Maximum Length Substring With Two Occurrences

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Find the maximum length of a contiguous substring where each character appears at most twice.

## 🔍 Key Observation

A sliding window can maintain a valid substring by expanding the right endpoint and shrinking the left endpoint whenever a character's frequency exceeds two.

## ⚙️ Algorithm

**Sliding window**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`sliding window` `two pointers` `hash table` `string`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d=Counter()
        l=0
        res=0
        for r in range(len(s)):
            d[s[r]]+=1
            while d[s[r]]>2:
                d[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
```

</details>
