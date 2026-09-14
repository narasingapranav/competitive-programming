# 🟠 max-consecutive-ones — Max Consecutive Ones

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/) &nbsp;|&nbsp; **Solved:** 2026-02-27

---

## 📝 Summary

Accepted solution for Max Consecutive Ones on LeetCode.

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
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pc=0
        mc=0
        for i in nums:
            if i==0:
                mc=max(mc,pc)
                pc=0
            else:
                pc+=1
        mc=max(mc,pc)
        return mc
```

</details>
