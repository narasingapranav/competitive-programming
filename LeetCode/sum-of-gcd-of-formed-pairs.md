# 🟠 sum-of-gcd-of-formed-pairs — Sum of GCD of Formed Pairs

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/) &nbsp;|&nbsp; **Solved:** 2026-07-16

---

## 📝 Summary

Accepted solution for Sum of GCD of Formed Pairs on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        gcdprefix = []
        mx = -1
        for i in nums:
            mx = max(mx, i)
            gcdprefix.append(gcd(i,mx))
        gcdprefix.sort()
        totalgcd = 0
        for i in range(len(gcdprefix)//2):
            totalgcd += gcd(gcdprefix[i], gcdprefix[-(i+1)])
        return totalgcd
```

</details>
