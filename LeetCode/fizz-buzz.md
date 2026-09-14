# 🟠 fizz-buzz — Fizz Buzz

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/fizz-buzz/) &nbsp;|&nbsp; **Solved:** 2025-12-20

---

## 📝 Summary

Accepted solution for Fizz Buzz on LeetCode.

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
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                a.append("FizzBuzz")
            elif i%3==0:
                a.append("Fizz")
            elif i%5==0:
                a.append("Buzz")
            else:
                a.append(str(i))
        return a
```

</details>
