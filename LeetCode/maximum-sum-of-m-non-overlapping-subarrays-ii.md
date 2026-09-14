# 🟠 maximum-sum-of-m-non-overlapping-subarrays-ii — Maximum Sum of M Non-Overlapping Subarrays II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/) &nbsp;|&nbsp; **Solved:** 2026-06-07

---

## 📝 Summary

Accepted solution for Maximum Sum of M Non-Overlapping Subarrays II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Binary search + Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^9) (estimated -- 9 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`binary-search` `graph`

<details>
<summary>💻 View solution</summary>

```python
from typing import List
from collections import deque

class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        
        def solve_lam(lam: int):
            """O(n) DP with penalty lam per subarray. Tie-break: prefer more subarrays."""
            n = len(nums)
            pre = [0] * (n + 1)
            for i in range(n):
                pre[i+1] = pre[i] + nums[i]

            NEG = float('-inf')
            dp_v = [NEG] * (n + 1)
            dp_c = [0]   * (n + 1)
            dp_v[0] = 0
            dq = deque()

            for i in range(1, n + 1):
                dp_v[i] = dp_v[i-1]
                dp_c[i] = dp_c[i-1]

                j = i - l
                if j >= 0 and dp_v[j] != NEG:
                    kv = dp_v[j] - pre[j]
                    kc = dp_c[j]
                    while dq and (dq[-1][1] < kv or
                                  (dq[-1][1] == kv and dq[-1][2] < kc)):
                        dq.pop()
                    dq.append((j, kv, kc))

                while dq and dq[0][0] < i - r:
                    dq.popleft()

                if dq:
                    _, kv, kc = dq[0]
                    cand_v = pre[i] + kv - lam
                    cand_c = kc + 1
                    if (cand_v > dp_v[i] or
                       (cand_v == dp_v[i] and cand_c > dp_c[i])):
                        dp_v[i] = cand_v
                        dp_c[i] = cand_c

            return dp_v[n], dp_c[n]

        def best_single():
            """Max subarray sum of length in [l,r] — used when all are negative."""
            n = len(nums)
            pre = [0] * (n + 1)
            for i in range(n):
                pre[i+1] = pre[i] + nums[i]
            dq = deque()
            best = float('-inf')
            for i in range(1, n + 1):
                j = i - l
                if j >= 0:
                    while dq and pre[dq[-1]] >= pre[j]:
                        dq.pop()
                    dq.append(j)
                while dq and dq[0] < i - r:
                    dq.popleft()
                if dq:
                    best = max(best, pre[i] - pre[dq[0]])
            return best

        # Step 1: unconstrained (lam=0) — greedily pick all positive-contribution subarrays
        val0, cnt0 = solve_lam(0)

        if cnt0 <= m:
            # Naturally uses <= m subarrays
            if cnt0 >= 1:
                return val0          # already optimal
            return best_single()    # all negative: must still pick 1

        # Step 2: unconstrained wants > m; WQS binary search for exactly m
        lo, hi = 0, 2 * 10**10
        while lo < hi:
            mid = (lo + hi + 1) // 2
            _, cnt = solve_lam(mid)
            if cnt >= m:
                lo = mid
            else:
                hi = mid - 1

        val, _ = solve_lam(lo)
        return val + lo * m         # undo penalty for exactly m subarrays
```

</details>
