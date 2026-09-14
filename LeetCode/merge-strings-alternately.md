# 🟠 merge-strings-alternately — Merge Strings Alternately

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/merge-strings-alternately/) &nbsp;|&nbsp; **Solved:** 2026-05-30

---

## 📝 Summary

Accepted solution for Merge Strings Alternately on LeetCode.

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
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        i=0
        while i<len(word1) or i<len(word2):
            if i<len(word1):
                res.append(word1[i])
            if i<len(word2):
                res.append(word2[i])
            i+=1
        return "".join(res)

```

</details>
