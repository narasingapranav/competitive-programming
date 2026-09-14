# 🟠 smallest-subsequence-of-distinct-characters — Smallest Subsequence of Distinct Characters

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/) &nbsp;|&nbsp; **Solved:** 2026-07-19

---

## 📝 Summary

Accepted solution for Smallest Subsequence of Distinct Characters on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq=Counter(s)
        seen=set()
        st=[]
        for i in s:
            freq[i]-=1
            if i in seen: 
                continue
            while st and st[-1]>i and freq[st[-1]]:
                seen.remove(st.pop())
            st.append(i)
            seen.add(i)
        return "".join(st)
        
```

</details>
