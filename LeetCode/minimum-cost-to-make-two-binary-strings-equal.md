# 🟠 minimum-cost-to-make-two-binary-strings-equal — Minimum Cost to Make Two Binary Strings Equal

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/) &nbsp;|&nbsp; **Solved:** 2026-05-02

---

## 📝 Summary

Accepted solution for Minimum Cost to Make Two Binary Strings Equal on LeetCode.

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
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        c = [0, 0]
        for a, b in zip(s, t):
            if a != b:
                c[int(a)] += 1
        c0, c1 = c
        res1 = (c0 + c1) * flipCost
        res2 = min(c0, c1) * swapCost + abs(c0 - c1) * flipCost
        res3 = min(c0, c1) * swapCost + abs(c0 - c1) // 2 * (swapCost + crossCost) +  abs(c0 - c1) % 2 * flipCost
        return min(res1, res2, res3)
```

</details>
