# 🟠 baseball-game — Baseball Game

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/baseball-game/) &nbsp;|&nbsp; **Solved:** 2026-07-06

---

## 📝 Summary

Accepted solution for Baseball Game on LeetCode.

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
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in operations:
            if i.lstrip("-").isdigit():
                    res.append(int(i))
            elif i=="C":
                res.pop()
            elif i=="D":
                res.append(2*res[-1])
            elif i=="+":
                res.append(res[-1]+res[-2])
        return sum(res)
```

</details>
