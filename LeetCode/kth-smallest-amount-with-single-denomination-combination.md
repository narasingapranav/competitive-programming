# 🟠 kth-smallest-amount-with-single-denomination-combination — Kth Smallest Amount With Single Denomination Combination

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/) &nbsp;|&nbsp; **Solved:** 2026-08-29

---

## 📝 Summary

Accepted solution for Kth Smallest Amount With Single Denomination Combination on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Binary search + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`binary-search` `sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
    
        A = []
        for x in coins:
            if all(x % c for c in A):
                A.append(x)
    
        def check(m):
            tot = 0
            for x in range(1, len(A) + 1):
                for c in combinations(A, x):
                    tot += m // lcm(*c) * pow(-1, x + 1)
            return tot >= k
    
        return bisect_left(range(k * A[0] + 1), True, lo=1, key=check)
```

</details>
