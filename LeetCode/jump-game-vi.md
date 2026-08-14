# 🟠 jump-game-vi — Jump Game VI

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/jump-game-vi/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Find the maximum score reachable from the first to the last index of an array, where you can jump at most k steps forward at a time and landing on an index adds its value to your score.

## 🔍 Key Observation

The maximum score to reach index i is nums[i] plus the maximum score among the previous k indices, which can be efficiently maintained using a priority queue to track the sliding window maximum.

## ⚙️ Algorithm

**Dynamic programming + Priority queue**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`dynamic-programming` `heap` `priority-queue` `sliding-window`

<details>
<summary>💻 View solution</summary>

```python
import heapq

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        pq = []
        heapq.heappush(pq, (-nums[0], 0))
        for i in range(1, n):
            while pq[0][1] < i - k:
                heapq.heappop(pq)
            score = -pq[0][0] + nums[i]
            heapq.heappush(pq, (-score, i))
        return score
```

</details>
