# 🟠 count-symmetric-integers —   Count Symmetric Integers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-symmetric-integers/) &nbsp;|&nbsp; **Solved:** 2025-09-04

---

## 📝 Summary

Accepted solution for   Count Symmetric Integers on LeetCode.

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
    def digitSum(self, n: int) -> int:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0: 
                mid = len(s) // 2
                left_sum = sum(int(d) for d in s[:mid])
                right_sum = sum(int(d) for d in s[mid:])
                if left_sum == right_sum:
                    count += 1
        return count

```

</details>
