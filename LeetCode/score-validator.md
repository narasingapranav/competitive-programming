# 🟠 score-validator — Score Validator

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/score-validator/) &nbsp;|&nbsp; **Solved:** 2026-05-23

---

## 📝 Summary

Accepted solution for Score Validator on LeetCode.

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
    def scoreValidator(self, events: list[str]) -> list[int]:
        score,counter=0,0
        for i in events :
            if i=="W":
                counter+=1
                if counter ==10:
                    return [score,counter]
            elif i=="WD" or i=="NB":
                score+=1
            else:
                score+=int(i)
        return [score,counter]
```

</details>
