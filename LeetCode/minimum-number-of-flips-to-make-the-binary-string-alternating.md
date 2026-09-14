# 🟠 minimum-number-of-flips-to-make-the-binary-string-alternating — Minimum Number of Flips to Make the Binary String Alternating

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Accepted solution for Minimum Number of Flips to Make the Binary String Alternating on LeetCode.

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
    def minFlips(self, s: str) -> int:
        ss = s+s
        temps_1 = []
        temps_2 = []
        for i in range(len(ss)):
            if i%2 == 0:
                 temps_1.append('0')
                 temps_2.append('1')
            else:
                temps_1.append('1')
                temps_2.append('0')
        temps_1 = ''.join(temps_1)
        temps_2 = ''.join(temps_2)
        l = 0
        diff1 = 0
        diff2 = 0
        ans  = float('inf')
        n = len(s)
        for r in range(len(ss)):
            if ss[r] != temps_1[r]:
                diff1+=1
            if ss[r] != temps_2[r]:
                diff2+=1

            if r-l+1 > n:
                if ss[l] != temps_1[l]:
                    diff1 -= 1
                if ss[l] != temps_2[l]:
                    diff2 -= 1
                l += 1

            if r-l+1 == n:
                ans = min(ans,diff1,diff2)
        return ans
```

</details>
