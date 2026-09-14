# 🟠 next-greater-element-ii — Next Greater Element II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/next-greater-element-ii/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Accepted solution for Next Greater Element II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        temp=nums+nums
        n=len(nums)
        res=[-1]*n
        stack=[]
        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if i < n:
                if stack:
                    res[i] = stack[-1]
            stack.append(nums[i % n])
        return res
```

</details>
