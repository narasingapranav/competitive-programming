# 🟠 number-of-different-subsequences-gcds — Number of Different Subsequences GCDs

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-different-subsequences-gcds/) &nbsp;|&nbsp; **Solved:** 2026-02-23

---

## 📝 Summary

Accepted solution for Number of Different Subsequences GCDs on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_num = max(nums)
        pres = [False]*(max_num +1)
        for num in nums:
            pres[num] = True
        count =0
        for d in range(1, max_num + 1):
            g =0 
            for j in range(d, max_num+1, d):
                if pres[j]:
                    g= gcd(g,j)
                    if g==d:
                        count += 1
                        break
        return count
```

</details>
