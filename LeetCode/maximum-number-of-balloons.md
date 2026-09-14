# 🟠 maximum-number-of-balloons — Maximum Number of Balloons

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/) &nbsp;|&nbsp; **Solved:** 2026-06-22

---

## 📝 Summary

Accepted solution for Maximum Number of Balloons on LeetCode.

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
    def maxNumberOfBalloons(self, text):
        b = a = l = o = n = 0

        for c in text:
            if c == 'b':
                b += 1
            elif c == 'a':
                a += 1
            elif c == 'l':
                l += 1
            elif c == 'o':
                o += 1
            elif c == 'n':
                n += 1

        return min(b, a, l // 2, o // 2, n)
```

</details>
