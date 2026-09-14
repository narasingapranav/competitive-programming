# 🟠 kth-largest-element-in-an-array — Kth Largest Element in an Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/) &nbsp;|&nbsp; **Solved:** 2025-12-15

---

## 📝 Summary

Accepted solution for Kth Largest Element in an Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q=[]
        for i in nums:
            heapq.heappush(q,-i)
        for i in range(k-1):
            heapq.heappop(q)
        return -1*heapq.heappop(q)
```

</details>
