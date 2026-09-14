# 🟠 count-array-pairs-divisible-by-k — Count Array Pairs Divisible by K

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-array-pairs-divisible-by-k/) &nbsp;|&nbsp; **Solved:** 2026-02-23

---

## 📝 Summary

Accepted solution for Count Array Pairs Divisible by K on LeetCode.

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
from math import gcd
from collections import Counter
from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        count = Counter()
        for num in nums:
            g = gcd(num, k)
            for i in count:
                if (g * i) % k == 0:
                    ans += count[i]
            count[g] += 1
        return ans
```

</details>
