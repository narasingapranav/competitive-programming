# 🟠 minimum-total-cost-to-process-all-elements — Minimum Total Cost to Process All Elements

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Accepted solution for Minimum Total Cost to Process All Elements on LeetCode.

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
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD=10**9 + 7
        res=k
        ops=0
        for i in nums:
            if res<i:
                req=(i-res+k-1)//k
                ops+=req
                res+=req*k
            res-=i
        return (ops*(ops+1)//2)%MOD
                
```

</details>
