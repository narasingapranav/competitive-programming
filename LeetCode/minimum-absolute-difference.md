# 🟠 minimum-absolute-difference — Minimum Absolute Difference

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-absolute-difference/) &nbsp;|&nbsp; **Solved:** 2026-01-26

---

## 📝 Summary

Accepted solution for Minimum Absolute Difference on LeetCode.

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
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m=min(arr[i+1]-arr[i] for i in range(len(arr)-1))
        return [[arr[i],arr[i+1]] for i in range(len(arr) -1) if arr[i+1]- arr[i]== m]
```

</details>
