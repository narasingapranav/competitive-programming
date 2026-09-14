# 🟠 capacity-to-ship-packages-within-d-days — Capacity To Ship Packages Within D Days

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) &nbsp;|&nbsp; **Solved:** 2026-08-11

---

## 📝 Summary

Accepted solution for Capacity To Ship Packages Within D Days on LeetCode.

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
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def solve(wei):
            total=1
            w=0
            for i in weights:
                if w+i>wei:
                    total+=1
                    w=i
                else:
                    w+=i
            return total
        l=max(weights)
        h=sum(weights)
        while l<h:
            mid=l+(h-l)//2
            if solve(mid)>days:
                l=mid+1
            else:
                h=mid
        return l
```

</details>
