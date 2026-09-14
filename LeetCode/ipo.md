# 🟠 ipo — IPO

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/ipo/) &nbsp;|&nbsp; **Solved:** 2026-02-26

---

## 📝 Summary

Accepted solution for IPO on LeetCode.

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
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        q=[]
        m=[]
        for i in range(len(profits)):
            heapq.heappush(q,(capital[i],profits[i]))
        for _ in range(k):
            while q and q[0][0]<=w:
                heapq.heappush(m,-heapq.heappop(q)[1])
            if not m:
                break
            w+= -heapq.heappop(m)
        return w
```

</details>
