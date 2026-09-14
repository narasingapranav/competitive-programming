# 🟠 password-strength — Password Strength

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/password-strength/) &nbsp;|&nbsp; **Solved:** 2026-05-24

---

## 📝 Summary

Accepted solution for Password Strength on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def passwordStrength(self, password: str) -> int:
        strength = 0
        seen = set()

        for ch in password:
            if ch not in seen:
                seen.add(ch)

                if 'a' <= ch <= 'z':
                    strength += 1

                elif 'A' <= ch <= 'Z':
                    strength += 2

                elif '0' <= ch <= '9':
                    strength += 3

                elif ch in "!@#$":
                    strength += 5

        return strength
```

</details>
