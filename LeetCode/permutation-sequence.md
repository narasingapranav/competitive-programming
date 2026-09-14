# 🟠 permutation-sequence — Permutation Sequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/permutation-sequence/) &nbsp;|&nbsp; **Solved:** 2025-12-18

---

## 📝 Summary

Accepted solution for Permutation Sequence on LeetCode.

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
    def getPermutation(self, n: int, k: int) -> str:
        used = [0] * n 
        result = ""

        k -= 1

        for i in range(n):
            s = math.factorial(n-i-1)
            x = int(k / s) + 1
            k = k % s
            c = 0
            t = -1
            while c < x:
                t += 1
                if not used[t]:
                    c += 1
            used[t] = 1
            result += str(t + 1)

        return result
```

</details>
