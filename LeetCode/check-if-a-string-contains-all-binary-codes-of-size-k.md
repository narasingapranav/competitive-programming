# 🟠 check-if-a-string-contains-all-binary-codes-of-size-k — Check If a String Contains All Binary Codes of Size K

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) &nbsp;|&nbsp; **Solved:** 2026-02-23

---

## 📝 Summary

Accepted solution for Check If a String Contains All Binary Codes of Size K on LeetCode.

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
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n - k + 1 < (1 << k):
            return False
        seen = set()
        for i in range(n - k + 1):
            seen.add(s[i:i+k])
        return len(seen) == (1 << k)
```

</details>
