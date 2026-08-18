# 🟠 constrained-subsequence-sum — Constrained Subsequence Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/constrained-subsequence-sum/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Find the maximum sum of a non-empty subsequence where the indices of any two consecutive elements in the subsequence differ by at most k.

## 🔍 Key Observation

The optimal subproblem solution for index i depends on adding nums[i] to the maximum positive subsequence sum ending in the window [i-k, i-1], which can be tracked efficiently using a monotonic queue.

## ⚙️ Algorithm

**Dynamic programming with monotonic queue**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(k)` |

## 🏷️ Tags

`dynamic-programming` `monotonic-queue` `sliding-window` `deque`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()
        res = float('-inf')
        for i, num in enumerate(nums):
            total = num + q[0][1] if q else num
            res = max(res, total)
            while q and total >= q[-1][1]:
                q.pop()
            if total > 0:
                q.append((i, total))
            if q and q[0][0] == i - k:
                q.popleft()
        return res        
```

</details>
