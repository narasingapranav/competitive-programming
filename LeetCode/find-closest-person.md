# 🟠 find-closest-person — Find Closest Person

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-closest-person/) &nbsp;|&nbsp; **Solved:** 2025-09-04

---

## 📝 Summary

Accepted solution for Find Closest Person on LeetCode.

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
    def findClosest(self, x: int, y: int, z: int) -> int:
        xz=abs(x-z)
        yz=abs(y-z)
        if xz==yz:
            return 0
        return 2 if xz>yz else 1
```

</details>
