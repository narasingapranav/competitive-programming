# 🟠 four-divisors — Four Divisors

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/four-divisors/) &nbsp;|&nbsp; **Solved:** 2026-01-04

---

## 📝 Summary

Accepted solution for Four Divisors on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            divisors = set()
            i = 1
            while i * i <= n:
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                    if len(divisors) > 4:
                        break
                i += 1
            if len(divisors) == 4:
                total += sum(divisors)
        return total

```

</details>
