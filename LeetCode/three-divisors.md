# 🟠 three-divisors — Three Divisors

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/three-divisors/) &nbsp;|&nbsp; **Solved:** 2025-10-11

---

## 📝 Summary

Accepted solution for Three Divisors on LeetCode.

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
    def isThree(self, n: int) -> bool:
        root = int(math.sqrt(n))
        if root * root != n:
            return False
        for i in range(2, int(math.sqrt(root)) + 1):
            if root % i == 0:
                return False
        return root > 1
```

</details>
