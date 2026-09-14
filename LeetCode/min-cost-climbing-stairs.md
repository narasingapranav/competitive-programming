# 🟠 min-cost-climbing-stairs — Min Cost Climbing Stairs

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/) &nbsp;|&nbsp; **Solved:** 2026-07-10

---

## 📝 Summary

Accepted solution for Min Cost Climbing Stairs on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 4, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])         
        return min(cost[0], cost[1])
```

</details>
