# 🟠 process-string-with-special-operations-ii — Process String with Special Operations II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/process-string-with-special-operations-ii/) &nbsp;|&nbsp; **Solved:** 2026-06-17

---

## 📝 Summary

Accepted solution for Process String with Special Operations II on LeetCode.

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
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        ln = 0

        for c in s:
            if c == '*':
                ln = max(ln - 1, 0)
            elif c == '#':
                ln *= 2
            elif c != '%':
                ln += 1

        if k >= ln:
            return '.'

        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == '*':
                ln += 1
            elif c == '#':
                if k >= ln // 2:
                    k -= ln // 2
                ln //= 2
            elif c == '%':
                k = ln - 1 - k
            else:
                if ln == k + 1:
                    return c
                ln -= 1
```

</details>
