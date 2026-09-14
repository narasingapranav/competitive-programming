# 🟠 add-digits — Add Digits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/add-digits/) &nbsp;|&nbsp; **Solved:** 2025-08-14

---

## 📝 Summary

Accepted solution for Add Digits on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) !=1 :
            rem=0
            sum=0
            while num >0:
                rem=num%10
                sum+=rem
                num//=10
            return self.addDigits(sum)
        else:
            return num
    
            
            
```

</details>
