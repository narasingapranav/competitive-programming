# 🟠 relative-ranks — Relative Ranks

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/relative-ranks/) &nbsp;|&nbsp; **Solved:** 2026-05-30

---

## 📝 Summary

Accepted solution for Relative Ranks on LeetCode.

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
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        sortedList = sorted(score, reverse=True)
        rank = {}
        for i in range(n):
            if i == 0:
                rank[sortedList[i]] = "Gold Medal"
            elif i == 1:
                rank[sortedList[i]] = "Silver Medal"
            elif i == 2:
                rank[sortedList[i]] = "Bronze Medal"
            else:
                rank[sortedList[i]] = str(i+1)
        ans = []
        for scr in score:
            ans.append(rank[scr])
        return ans
```

</details>
