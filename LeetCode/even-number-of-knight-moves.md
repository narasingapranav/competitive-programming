# 🟠 even-number-of-knight-moves — Even Number of Knight Moves

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/even-number-of-knight-moves/) &nbsp;|&nbsp; **Solved:** 2026-07-19

---

## 📝 Summary

Accepted solution for Even Number of Knight Moves on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return (start[1]+start[0])%2==(target[0]+target[1])%2
```

</details>
