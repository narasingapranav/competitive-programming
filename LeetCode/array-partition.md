# 🟠 array-partition — Array Partition

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/array-partition/) &nbsp;|&nbsp; **Solved:** 2025-11-20

---

## 📝 Summary

Accepted solution for Array Partition on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        a=[]
        for i in range(0,len(nums),2):
            a.append((nums[i],nums[i+1]))
        s=0
        for i in a:
            s+=min(i)
        return s
```

</details>
