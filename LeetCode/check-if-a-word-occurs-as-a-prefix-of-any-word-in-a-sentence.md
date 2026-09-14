# 🟠 check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence — Check If a Word Occurs As a Prefix of Any Word in a Sentence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/) &nbsp;|&nbsp; **Solved:** 2025-10-11

---

## 📝 Summary

Accepted solution for Check If a Word Occurs As a Prefix of Any Word in a Sentence on LeetCode.

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
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        w=sentence.split()
        for i,j in enumerate(w):
            if j.startswith(searchWord):
                return i+1
        return -1

```

</details>
