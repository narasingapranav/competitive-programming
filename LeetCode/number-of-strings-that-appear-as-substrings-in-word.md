# 🟠 number-of-strings-that-appear-as-substrings-in-word — Number of Strings That Appear as Substrings in Word

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Accepted solution for Number of Strings That Appear as Substrings in Word on LeetCode.

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
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for p in patterns:
            if p in word:
                count += 1
        return count
```

</details>
