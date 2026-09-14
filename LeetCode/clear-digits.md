# 🟠 clear-digits — Clear Digits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/clear-digits/) &nbsp;|&nbsp; **Solved:** 2025-12-13

---

## 📝 Summary

Accepted solution for Clear Digits on LeetCode.

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
    def clearDigits(self, s: str) -> str:
        res=[]
        for i in s:
            if i.isdigit():
                res.pop()
            else:
                res.append(i)
        return "".join(res)
```

</details>
