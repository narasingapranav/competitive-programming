# 🟠 number-of-common-factors — Number of Common Factors

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-common-factors/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Accepted solution for Number of Common Factors on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    def commonFactors(self, a: int, b: int) -> int:
        g = self.gcd(a, b)
        count = 0
        for i in range(1, int(g**0.5) + 1):
            if g % i == 0:
                count += 1
                if i != g // i:
                    count += 1   
        return count
```

</details>
