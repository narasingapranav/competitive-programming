# 🟠 longest-substring-without-repeating-characters — Longest Substring Without Repeating Characters

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/) &nbsp;|&nbsp; **Solved:** 2026-07-22

---

## 📝 Summary

Accepted solution for Longest Substring Without Repeating Characters on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxlen=0
        se=set()
        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l+=1
            se.add(s[r])
            maxlen=max(maxlen,r-l+1)
        return maxlen
            
```

</details>
