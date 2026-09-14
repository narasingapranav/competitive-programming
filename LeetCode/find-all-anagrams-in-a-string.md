# 🟠 find-all-anagrams-in-a-string — Find All Anagrams in a String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/) &nbsp;|&nbsp; **Solved:** 2026-07-23

---

## 📝 Summary

Accepted solution for Find All Anagrams in a String on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=sorted(p)
        l=len(p)
        res=[]
        for i in range(len(s)-l+1):
            if sorted(s[i:i+l])==p:
                res.append(i)
        return res
```

</details>
