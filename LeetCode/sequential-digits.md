# 🟠 sequential-digits — Sequential Digits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sequential-digits/) &nbsp;|&nbsp; **Solved:** 2026-07-13

---

## 📝 Summary

Accepted solution for Sequential Digits on LeetCode.

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
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        s="123456789"
        l=str(low)
        h=str(high)
        for i in range(len(l),len(h)+1):
            for j in range(10-i):
                n=int(s[j:j+i])
                if low<=n<=high:
                    res.append(n)
        return res
```

</details>
