# 🟠 number-of-different-subsequences-gcds — Number of Different Subsequences GCDs

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-different-subsequences-gcds/) &nbsp;|&nbsp; **Solved:** 2026-02-23

---

## 📝 Summary

Accepted solution for Number of Different Subsequences GCDs on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion + Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`recursion` `hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def gcd(self,a,b):
        if b==0:
            return a
        return gcd(b,a%b)
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_val = max(nums)
        num_set = set(nums)
        ans = 0
        for x in range(1, max_val + 1):
            g = 0
            for multiple in range(x, max_val + 1, x):
                if multiple in num_set:
                    g = self.gcd(g, multiple)
                if g == x:
                    ans += 1
                    break
        return ans
```

</details>
