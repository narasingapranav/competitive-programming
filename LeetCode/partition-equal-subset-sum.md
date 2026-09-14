# 🟠 partition-equal-subset-sum — Partition Equal Subset Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Accepted solution for Partition Equal Subset Sum on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t=sum(nums)
        if t%2 !=0:
            return False
        tar=t//2
        p={0}
        for i in nums:
            n=set()
            for j in p:
                n.add(i+j)
            p|=n
        return tar in p
```

</details>
