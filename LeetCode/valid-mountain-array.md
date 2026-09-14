# 🟠 valid-mountain-array — Valid Mountain Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/valid-mountain-array/) &nbsp;|&nbsp; **Solved:** 2026-05-18

---

## 📝 Summary

Accepted solution for Valid Mountain Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0

        # 1. Climb up
        while i+1 < n and arr[i] < arr[i+1]:
            i += 1

        # 2. Peak check: Peak can't be first or last element
        if i == 0 or i == n-1:
            return False

        # 3. Climb down
        while i+1 < n and arr[i] > arr[i+1]:
            i += 1

        # 4. If we reached the end, it's a mountain
        return i == n-1
```

</details>
