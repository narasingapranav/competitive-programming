# 🟠 minimum-initial-energy-to-finish-tasks — Minimum Initial Energy to Finish Tasks

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/) &nbsp;|&nbsp; **Solved:** 2026-05-12

---

## 📝 Summary

Accepted solution for Minimum Initial Energy to Finish Tasks on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Binary search + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`binary-search` `sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumEffort(self, shop: list[list[int]]) -> int:
        shop.sort(key=lambda x: x[1] - x[0], reverse=True)
        def test(bal):
            for cost, thresh in shop:
                if bal < thresh:
                    return False
                bal -= cost
            return True
        return bisect.bisect_left(range(10**9 + 1), True, key=test)

```

</details>
