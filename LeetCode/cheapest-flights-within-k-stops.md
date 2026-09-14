# 🟠 cheapest-flights-within-k-stops — Cheapest Flights Within K Stops

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Accepted solution for Cheapest Flights Within K Stops on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Dynamic programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n²) (estimated -- DP table detected)` | `~O(n) (estimated)` |

## 🏷️ Tags

`dp`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # as we want min initialize all to max
        dp=[float("inf")]*n
        # src -> src cost =0
        dp[src]=0
        # k stops
        for _ in range(k+1):
            temp=dp.copy()
            for st,en,cos in flights:
                # if min go to min path
                if dp[st]!=float("inf"):
                    temp[en]=min(temp[en],dp[st]+cos)
            dp=temp
        return dp[dst] if dp[dst] !=float("inf") else -1
```

</details>
