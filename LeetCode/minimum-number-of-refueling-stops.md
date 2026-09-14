# 🟠 minimum-number-of-refueling-stops — Minimum Number of Refueling Stops

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-refueling-stops/) &nbsp;|&nbsp; **Solved:** 2026-05-02

---

## 📝 Summary

Accepted solution for Minimum Number of Refueling Stops on LeetCode.

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
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, st: List[List[int]]) -> int:
        heap=[]
        fuel=startFuel
        n=len(st)
        stopC=0
        i=0
        while fuel<target:
            while i<n and st[i][0]<=fuel:
                heapq.heappush(heap,-st[i][1])
                i+=1
            if not heap:
                return -1
            fuel+= -heapq.heappop(heap)
            stopC+=1
        return stopC
```

</details>
