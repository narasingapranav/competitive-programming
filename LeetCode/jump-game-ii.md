# 🟠 jump-game-ii — Jump Game II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/jump-game-ii/) &nbsp;|&nbsp; **Solved:** 2026-02-26

---

## 📝 Summary

Accepted solution for Jump Game II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        curEnd=0
        far=0
        n=len(nums)
        for i in range(n-1):
            far=max(far,i+nums[i])
            if i==curEnd:
                jumps+=1
                curEnd=far
        return jumps
```

</details>
