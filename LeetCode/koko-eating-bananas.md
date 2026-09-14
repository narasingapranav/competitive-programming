# 🟠 koko-eating-bananas — Koko Eating Bananas

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/koko-eating-bananas/) &nbsp;|&nbsp; **Solved:** 2026-02-25

---

## 📝 Summary

Accepted solution for Koko Eating Bananas on LeetCode.

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
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        low=1
        high=max(piles)
        while low<high:
            mid= low +(high-low)//2
            a=0
            for i in piles:
                a+=math.ceil(i/mid)
            if a<=h:
                high=mid
            else:
                low=mid+1
        return low
```

</details>
