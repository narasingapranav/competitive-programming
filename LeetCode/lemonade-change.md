# 🟠 lemonade-change — Lemonade Change

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/lemonade-change/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Accepted solution for Lemonade Change on LeetCode.

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
    def lemonadeChange(self, bills: List[int]) -> bool:
        f,te,tw=0,0,0
        if bills[0]!=5:
            return False
        for i in bills:
            if i==5:
                f+=1
            elif i==10:
                if f>=1:
                    f-=1
                    te+=1
                else:
                    return False
            else:
                if te>=1 and f>=1:
                    te-=1
                    f-=1
                    tw+=1
                elif f>=3:
                    f-=3
                else:
                    return False
        return True
```

</details>
