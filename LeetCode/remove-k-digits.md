# 🟠 remove-k-digits — Remove K Digits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-k-digits/) &nbsp;|&nbsp; **Solved:** 2026-02-26

---

## 📝 Summary

Accepted solution for Remove K Digits on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in num:
            while st and k>0 and st[-1]>i:
                st.pop()
                k-=1
            st.append(i)
        while k>0:
            st.pop()
            k-=1
        res= "".join(st).lstrip('0')
        return res if res!="" else '0'
```

</details>
