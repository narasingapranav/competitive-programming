# 🟠 delete-columns-to-make-sorted — Delete Columns to Make Sorted

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/delete-columns-to-make-sorted/) &nbsp;|&nbsp; **Solved:** 2025-12-21

---

## 📝 Summary

Accepted solution for Delete Columns to Make Sorted on LeetCode.

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
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(col!=sorted(col) for col in map(list,zip(*strs)))
```

</details>
