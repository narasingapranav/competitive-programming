# 🟠 minimum-number-of-days-to-make-m-bouquets — Minimum Number of Days to Make m Bouquets

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) &nbsp;|&nbsp; **Solved:** 2026-02-25

---

## 📝 Summary

Accepted solution for Minimum Number of Days to Make m Bouquets on LeetCode.

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
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        while low<=high:
            mid= low + (high-low)//2
            boq=0
            con=0
            for i in range(0,len(bloomDay)):
                if bloomDay[i]<=mid:
                    con+=1
                    if con==k:
                        boq+=1
                        con=0
                else:
                    con=0
            if boq>=m:
                high=mid-1
            else:
                low=mid+1
        return low

```

</details>
