# 🟠 maximum-square-area-by-removing-fences-from-a-field — Maximum Square Area by Removing Fences From a Field

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/) &nbsp;|&nbsp; **Solved:** 2026-01-17

---

## 📝 Summary

Accepted solution for Maximum Square Area by Removing Fences From a Field on LeetCode.

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
    def maximizeSquareArea(
        self,
        m: int,
        n: int,
        hFences: List[int],
        vFences: List[int],
    ) -> int:
        MOD = 10**9+7
        
        # add boundaries
        hF = [1] + sorted(hFences) + [m]
        vF = [1] + sorted(vFences) + [n]
        
        # compute all horizontal distances
        hGaps = {hF[j] - hF[i] for i in range(len(hF)) for j in range(i+1, len(hF))}
        
        # compute all vertical distances
        vGaps = {vF[j] - vF[i] for i in range(len(vF)) for j in range(i+1, len(vF))}
        
        # find common distances
        common = hGaps & vGaps
        
        if not common:
            return -1
        
        max_side = max(common)
        return (max_side * max_side) % MOD
```

</details>
