# 🟠 check-if-binary-string-has-at-most-one-segment-of-ones — Check if Binary String Has at Most One Segment of Ones

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/) &nbsp;|&nbsp; **Solved:** 2026-03-06

---

## 📝 Summary

Accepted solution for Check if Binary String Has at Most One Segment of Ones on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        for i in range(1,len(s)):
            if s[i]== '1' and s[i-1]=='0' :
                return False
        return True
```

</details>
