# 🟠 minimum-window-substring — Minimum Window Substring

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-window-substring/) &nbsp;|&nbsp; **Solved:** 2026-02-25

---

## 📝 Summary

Accepted solution for Minimum Window Substring on LeetCode.

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
    def minWindow(self, s: str, t: str) -> str:
        m=len(s)
        n=len(t)
        if m<n:
            return ""
        dic={}
        for c in t:
            dic[c]=dic.get(c,0)+1
        print(dic)
        req=len(dic)
        formed=0
        left=0
        win={}
        start=0
        minlen=float('inf')
        for r in range(len(s)):
            win[s[r]] = win.get(s[r], 0) + 1
            if s[r] in dic and win[s[r]]==dic[s[r]]:
                formed+=1
            while formed==req:
                if r-left+1<minlen:
                    minlen=r-left+1
                    start=left
                win[s[left]]-=1
                if s[left] in dic and win[s[left]] <dic[s[left]] :
                    formed-=1
                left+=1
        return "" if minlen==float('inf') else s[start:start+minlen]
```

</details>
