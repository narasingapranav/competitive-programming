# 🟠 check-good-integer — Check Good Integer

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-good-integer/) &nbsp;|&nbsp; **Solved:** 2026-06-15

---

## 📝 Summary

Accepted solution for Check Good Integer on LeetCode.

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
    def checkGoodInteger(self, n: int) -> bool:
        sum_ = 0
        squaresum = 0
        while(n):
            rem = n%10
            sum_ += rem
            squaresum += (rem**2)
            n = n//10
        return squaresum - sum_ >= 50
```

</details>
