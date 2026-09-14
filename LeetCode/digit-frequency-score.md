# 🟠 digit-frequency-score — Digit Frequency Score

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/digit-frequency-score/) &nbsp;|&nbsp; **Solved:** 2026-05-31

---

## 📝 Summary

Accepted solution for Digit Frequency Score on LeetCode.

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
    def digitFrequencyScore(self, n: int) -> int:
        score = 0
        while n > 0:
            score += n % 10
            n //= 10
        return score
```

</details>
