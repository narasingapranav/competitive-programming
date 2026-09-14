# 🟠 make-lexicographically-smallest-array-by-swapping-elements — Make Lexicographically Smallest Array by Swapping Elements

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/) &nbsp;|&nbsp; **Solved:** 2026-08-29

---

## 📝 Summary

Accepted solution for Make Lexicographically Smallest Array by Swapping Elements on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def lexicographicallySmallestArray(self, A: list[int], limit: int) -> list[int]:
        groups = []
        gmap = {}

        for val in sorted(A):
            if not groups or val - groups[-1][-1] > limit:
                groups.append([])
            groups[-1].append(val)
            gmap[val] = len(groups) - 1

        itr = [iter(g) for g in groups]

        for i in range(len(A)):
            A[i] = next(itr[gmap[A[i]]])

        return A
```

</details>
