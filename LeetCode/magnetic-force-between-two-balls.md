# 🟠 magnetic-force-between-two-balls — Magnetic Force Between Two Balls

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/magnetic-force-between-two-balls/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Accepted solution for Magnetic Force Between Two Balls on LeetCode.

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
import math
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def solve(dist):
            c=1
            last=position[0]
            for i in position[1:]:
                if i-last>=dist:
                    c+=1
                    last=i
                    if c==m:
                        return True
            return False
        position.sort()
        l=0
        h=position[-1]-position[0]
        while l<=h:
            mid=l+(h-l)//2
            if solve(mid):
                l=mid+1
            else:
                h=mid-1
        return h
```

</details>
