# 🟠 minimum-operations-to-sort-a-permutation — Minimum Operations to Sort a Permutation

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/) &nbsp;|&nbsp; **Solved:** 2026-05-24

---

## 📝 Summary

Accepted solution for Minimum Operations to Sort a Permutation on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```python
from collections import deque
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Check ascending circular form: [s, s+1, ...]
        s = (nums[0] - 0) % n
        if all(nums[i] == (i + s) % n for i in range(n)):
            start = (0, s)
        else:
            # Check descending circular form
            c = (nums[0] + 0) % n
            if all((nums[i] + i) % n == c for i in range(n)):
                s = (c - (n - 1)) % n
                start = (1, s)
            else:
                return -1

        target = (0, 0)

        q = deque([(start[0], start[1], 0)])
        visited = {start}

        while q:
            rev, shift, steps = q.popleft()

            if (rev, shift) == target:
                return steps

            if rev == 0:
                nxt1 = (0, (shift + 1) % n)   # rotate left
                nxt2 = (1, shift)             # reverse
            else:
                nxt1 = (1, (shift - 1) % n)   # rotate left
                nxt2 = (0, shift)             # reverse

            for nxt in (nxt1, nxt2):
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt[0], nxt[1], steps + 1))

        return -1
```

</details>
