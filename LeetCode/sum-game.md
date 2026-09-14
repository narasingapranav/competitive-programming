# 🟠 sum-game — Sum Game

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sum-game/) &nbsp;|&nbsp; **Solved:** 2026-08-23

---

## 📝 Summary

Accepted solution for Sum Game on LeetCode.

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
    def sumGame(self, num: str) -> bool:
        n = len(num)

        q1 = q2 = 0
        s1 = s2 = 0

        for i in range(n // 2):
            if num[i] == '?':
                q1 += 1
            else:
                s1 += int(num[i])

        for i in range(n // 2, n):
            if num[i] == '?':
                q2 += 1
            else:
                s2 += int(num[i])

        if (q1 + q2) % 2:
            return True

        return 2 * (s1 - s2) != 9 * (q2 - q1)
```

</details>
