# 🟠 jump-game-ii — Jump Game II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/jump-game-ii/) &nbsp;|&nbsp; **Solved:** 2026-07-11

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
    def jump(self, nums: List[int]) -> int: # [2,3,1,1,4]
        jumps=0 
        curEnd=0
        far=0
        n=len(nums)  # 5
        for i in range(n-1): #           0 | 1     | 2     | 3
            far=max(far,i+nums[i]) #     2 |     4 | 4     | 4
            if i==curEnd: #           true | false | true  | false
                jumps+=1 #               1 | skip  | 2     | skip
                curEnd=far #             2 | skip  | 4     | skip
        return jumps
```

</details>
