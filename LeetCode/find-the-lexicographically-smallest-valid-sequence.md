# 🟠 find-the-lexicographically-smallest-valid-sequence — Find the Lexicographically Smallest Valid Sequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Accepted solution for Find the Lexicographically Smallest Valid Sequence on LeetCode.

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
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n,m=len(word1),len(word2)
        last=[-1]*m
        i=n-1
        j=m-1
        while i>=0 and j>=0:
            if word1[i]==word2[j]:
                last[j]=i
                j-=1
            i-=1
        ans=[0]*m
        canchange=True
        j=0
        i=0
        while i<n and j<m:
            if word1[i]==word2[j]:
                ans[j]=i
                j+=1
            elif canchange and (j==m-1 or i<last[j+1]):
                ans[j]=i
                j+=1
                canchange=False
            if j==m:
                return ans
            i+=1
        return []
```

</details>
