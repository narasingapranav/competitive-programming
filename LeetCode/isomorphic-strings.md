# 🟠 isomorphic-strings — Isomorphic Strings

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/isomorphic-strings/) &nbsp;|&nbsp; **Solved:** 2025-08-15

---

## 📝 Summary

Accepted solution for Isomorphic Strings on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        ms={}
        mt={}
        for i,j in zip(s,t):
            if i in ms and ms[i]!=j:
                return False
            if j in mt and mt[j]!=i:
                return False
            ms[i]=j
            mt[j]=i
        return True
```

</details>
