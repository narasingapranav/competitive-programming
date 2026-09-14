# 🟠 subarray-sum-equals-k — Subarray Sum Equals K

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/) &nbsp;|&nbsp; **Solved:** 2026-04-30

---

## 📝 Summary

Accepted solution for Subarray Sum Equals K on LeetCode.

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
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        d[0]=1
        presum=0
        counter=0
        for e in nums:
            presum+=e
            temp=presum-k
            if temp in d:
                counter+=d[temp]
            d[presum]=d.get(presum,0)+1
        return counter
```

</details>
