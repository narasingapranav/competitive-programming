# 🟠 total-waviness-of-numbers-in-range-i — Total Waviness of Numbers in Range I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Accepted solution for Total Waviness of Numbers in Range I on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for num in range(num1, num2 + 1):
            s = str(num)
            if len(s) < 3:
                continue
            for i in range(1, len(s) - 1):
                left = int(s[i - 1])
                curr = int(s[i])
                right = int(s[i + 1])
                if (curr > left and curr > right) or (curr < left and curr < right):
                    total += 1
        return total
```

</details>
