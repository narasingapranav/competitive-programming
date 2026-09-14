# 🟠 concatenation-of-consecutive-binary-numbers — Concatenation of Consecutive Binary Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/) &nbsp;|&nbsp; **Solved:** 2026-02-28

---

## 📝 Summary

Accepted solution for Concatenation of Consecutive Binary Numbers on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def convertbin(self,n):
        s=''
        while n>0:
            s+=str(n%2)
            n//=2
        return s[::-1]
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        arr = []
        for i in range(1, n + 1):
            arr.append(self.convertbin(i))
        a = ''.join(arr)
        return int(a, 2) % MOD
```

</details>
