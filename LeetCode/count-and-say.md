# 🟠 count-and-say — Count and Say

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-and-say/) &nbsp;|&nbsp; **Solved:** 2026-07-14

---

## 📝 Summary

Accepted solution for Count and Say on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def find(self,s):
        count=1
        res=""
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                res+=str(count)+s[i-1]
                count=1
        res+=str(count)+s[-1]
        return res
    def countAndSay(self, n: int) -> str:
        res="1"
        for i in range(1,n):
            res=self.find(res)
        return res

```

</details>
