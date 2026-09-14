# 🟠 decode-ways — Decode Ways

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/decode-ways/) &nbsp;|&nbsp; **Solved:** 2026-07-10

---

## 📝 Summary

Accepted solution for Decode Ways on LeetCode.

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
    def numDecodings(self, s: str) -> int:
        prev, prevprev = 0, 0
        if s[0] == "0":
            return 0

        prev, prevprev = 1, 1
        for i in range(1, len(s)):
            curr = 0
            if s[i] != "0":
                curr = prev

            if s[i - 1] == "1" or (
                s[i - 1] == "2" and s[i] in ["0", "1", "2", "3", "4", "5", "6"]
            ):
                curr += prevprev

            prevprev = prev
            prev = curr

        return prev
```

</details>
