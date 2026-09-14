# 🟠 find-the-length-of-the-longest-common-prefix — Find the Length of the Longest Common Prefix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/) &nbsp;|&nbsp; **Solved:** 2026-05-21

---

## 📝 Summary

Accepted solution for Find the Length of the Longest Common Prefix on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        p=set()
        for num in arr1:
            s=str(num)
            for i in range(1,len(s)+1):
                p.add(s[:i])
        ans=0
        for num in arr2:
            s=str(num)
            for i in range(1,len(s)+1):
                if s[:i] in p:
                    ans=max(ans,i)
        return ans
```

</details>
