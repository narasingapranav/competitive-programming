# 🟠 the-kth-factor-of-n — The kth Factor of n

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/the-kth-factor-of-n/) &nbsp;|&nbsp; **Solved:** 2025-10-11

---

## 📝 Summary

Accepted solution for The kth Factor of n on LeetCode.

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
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        return -1    
```

</details>
