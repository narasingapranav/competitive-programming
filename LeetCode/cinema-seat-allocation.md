# 🟠 cinema-seat-allocation — Cinema Seat Allocation

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/cinema-seat-allocation/) &nbsp;|&nbsp; **Solved:** 2026-08-19

---

## 📝 Summary

Accepted solution for Cinema Seat Allocation on LeetCode.

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
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        c = defaultdict(int)
        for r, s in reservedSeats:
            if 1 < s < 10:
                c[r] |= 1 << (s-2)
        return (n-len(c))*2 + sum(0 in (r&15, r&60, r&240) for r in c.values())
```

</details>
