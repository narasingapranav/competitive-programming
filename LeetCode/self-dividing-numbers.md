# 🟠 self-dividing-numbers — Self Dividing Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/self-dividing-numbers/) &nbsp;|&nbsp; **Solved:** 2026-05-27

---

## 📝 Summary

Accepted solution for Self Dividing Numbers on LeetCode.

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
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isself(n):
            a=str(n)
            for i in a:
                if i=='0' or  n%int(i)!=0:
                    return False
            return True
        res=[]
        for i in range(left,right+1):
            if isself(i):
                res.append(i)
        return res
```

</details>
