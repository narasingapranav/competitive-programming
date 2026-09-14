# 🟠 minimum-deletions-to-make-string-balanced — Minimum Deletions to Make String Balanced

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/) &nbsp;|&nbsp; **Solved:** 2026-02-07

---

## 📝 Summary

Accepted solution for Minimum Deletions to Make String Balanced on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Dynamic programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n²) (estimated -- DP table detected)` | `~O(n) (estimated)` |

## 🏷️ Tags

`dp`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp=0
        count=0
        for c in s:
            if c == 'b':
                count+=1
            else:
                dp=min(dp+1,count)
        return dp
```

</details>
