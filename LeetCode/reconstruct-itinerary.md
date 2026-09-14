# 🟠 reconstruct-itinerary — Reconstruct Itinerary

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reconstruct-itinerary/) &nbsp;|&nbsp; **Solved:** 2026-05-15

---

## 📝 Summary

Accepted solution for Reconstruct Itinerary on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
import heapq
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        l=["JFK"]
        res=[]
        al=defaultdict(list)
        for s,e in tickets:
            heapq.heappush(al[s],e)
        while l:
            while al[l[-1]]:
                l.append(heapq.heappop(al[l[-1]]))
            res.append(l.pop())
        return res[::-1]
```

</details>
