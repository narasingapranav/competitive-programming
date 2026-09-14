# 🟠 longest-balanced-substring-i — Longest Balanced Substring I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-balanced-substring-i/) &nbsp;|&nbsp; **Solved:** 2026-02-12

---

## 📝 Summary

Accepted solution for Longest Balanced Substring I on LeetCode.

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
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            cnt = [0]*26        
            mx = 0            
            v = 0               
            for j in range(i, n):
                c = ord(s[j]) - ord('a')
                cnt[c] += 1
                if cnt[c] == 1:
                    v += 1
                mx = max(mx, cnt[c])
                if mx * v == j - i + 1:
                    ans = max(ans, j - i + 1)

        return ans
```

</details>
