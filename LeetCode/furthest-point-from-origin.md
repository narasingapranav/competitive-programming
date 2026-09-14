# 🟠 furthest-point-from-origin — Furthest Point From Origin

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/furthest-point-from-origin/) &nbsp;|&nbsp; **Solved:** 2026-04-24

---

## 📝 Summary

Accepted solution for Furthest Point From Origin on LeetCode.

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
    def furthestDistanceFromOrigin(self, m: str) -> int:
        return (d:=Counter(m)) and (abs(d['L']-d['R'])+d['_'])
```

</details>
