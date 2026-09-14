# 🟠 find-the-highest-altitude — Find the Highest Altitude

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-highest-altitude/) &nbsp;|&nbsp; **Solved:** 2026-06-19

---

## 📝 Summary

Accepted solution for Find the Highest Altitude on LeetCode.

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
    def largestAltitude(self, gain):
        n = len(gain)
        mx = 0

        for i in range(n + 1):
            alt = 0
            for j in range(i):
                alt += gain[j]
            mx = max(mx, alt)

        return mx
```

</details>
