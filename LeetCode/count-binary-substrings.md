# 🟠 count-binary-substrings — Count Binary Substrings

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-binary-substrings/) &nbsp;|&nbsp; **Solved:** 2026-02-19

---

## 📝 Summary

Accepted solution for Count Binary Substrings on LeetCode.

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
    def countBinarySubstrings(self, s: str) -> int:
        prev_group = 0
        curr_group = 1
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_group += 1
            else:
                result += min(prev_group, curr_group)
                prev_group = curr_group
                curr_group = 1

        result += min(prev_group, curr_group)
        return result
```

</details>
