# 🟠 total-hamming-distance — Total Hamming Distance

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/total-hamming-distance/) &nbsp;|&nbsp; **Solved:** 2025-12-08

---

## 📝 Summary

Accepted solution for Total Hamming Distance on LeetCode.

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
from itertools import combinations
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for bit in range(32):
            ones = 0
            mask = 1 << bit
            for num in nums:
                if num & mask:
                    ones += 1

            zeros = n - ones
            ans += ones * zeros

        return ans
```

</details>
