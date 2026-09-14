# 🟠 camelcase-matching — Camelcase Matching

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/camelcase-matching/) &nbsp;|&nbsp; **Solved:** 2025-10-11

---

## 📝 Summary

Accepted solution for Camelcase Matching on LeetCode.

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
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query, pattern):
            j = 0  # pointer for pattern
            for c in query:
                if j < len(pattern) and c == pattern[j]:
                    j += 1
                elif c.isupper():
                    return False
            return j == len(pattern)

        return [match(q, pattern) for q in queries]        
```

</details>
