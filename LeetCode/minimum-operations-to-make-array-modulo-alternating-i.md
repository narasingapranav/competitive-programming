# 🟠 minimum-operations-to-make-array-modulo-alternating-i — Minimum Operations to Make Array Modulo Alternating I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/) &nbsp;|&nbsp; **Solved:** 2026-05-23

---

## 📝 Summary

Accepted solution for Minimum Operations to Make Array Modulo Alternating I on LeetCode.

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
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n=len(nums)
        ans=float('inf')
        for x in range(k):
            for y in range(k):
                if x==y:
                    continue
                cost=0
                for i in range(n):
                    target=x if i%2==0 else y
                    r=nums[i]%k
                    cost+=min((r-target)%k,(target-r)%k)
                ans=min(ans,cost)
        return ans
```

</details>
