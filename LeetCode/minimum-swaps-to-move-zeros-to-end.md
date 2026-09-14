# 🟠 minimum-swaps-to-move-zeros-to-end — Minimum Swaps to Move Zeros to End

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/) &nbsp;|&nbsp; **Solved:** 2026-05-23

---

## 📝 Summary

Accepted solution for Minimum Swaps to Move Zeros to End on LeetCode.

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
    def minimumSwaps(self, nums: list[int]) -> int:
        n=len(nums)
        z=nums.count(0)
        a=0
        for i in range(n-z,n):
            if nums[i]==0:
                a+=1
        return z-a
```

</details>
