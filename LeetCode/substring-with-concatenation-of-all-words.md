# 🟠 substring-with-concatenation-of-all-words — Substring with Concatenation of All Words

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) &nbsp;|&nbsp; **Solved:** 2026-08-11

---

## 📝 Summary

Accepted solution for Substring with Concatenation of All Words on LeetCode.

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
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordlen=len(words[0])
        l=0
        n=len(words)
        totallen=wordlen*n
        res=[]
        d={}
        for i in words:
            d[i]=d.get(i,0)+1
        for i in range(wordlen):
            l=i
            c=0
            curr={}
            for r in range(i,len(s)-wordlen+1,wordlen):
                present=s[r:r+wordlen]
                if present in d:
                    curr[present]=curr.get(present,0)+1
                    c+=1
                    while curr[present]>d[present]:
                        lw=s[l:l+wordlen]
                        curr[lw]-=1
                        l+=wordlen
                        c-=1
                    if c==n:
                        res.append(l)
                else:
                    curr.clear()
                    c=0
                    l=r+wordlen
        return res
```

</details>
