# 🟠 set-mismatch — Set Mismatch

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/set-mismatch/) &nbsp;|&nbsp; **Solved:** 2025-12-20

---

## 📝 Summary

Accepted solution for Set Mismatch on LeetCode.

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
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set()
        duplicate = -1
        for num in nums:
            if num in num_set:
                duplicate = num
            else:
                num_set.add(num)
        total_sum = n * (n + 1) // 2
        missing = total_sum - (sum(nums) - duplicate)
        
        return [duplicate, missing]
```

</details>
