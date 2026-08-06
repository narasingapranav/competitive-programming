# 🟠 palindrome-partitioning — Palindrome Partitioning

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/palindrome-partitioning/) &nbsp;|&nbsp; **Solved:** 2026-08-06

---

## 📝 Summary

Partition a given string into all possible sets of substrings such that every substring in a partition is a palindrome.

## 🔍 Key Observation

By using backtracking, we can systematically explore all valid partitions starting from the beginning of the string, only recursing deeper when the current prefix substring is a valid palindrome.

## ⚙️ Algorithm

**Backtracking**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N * 2^N)` | `O(N)` |

## 🏷️ Tags

`backtracking` `string` `dfs`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalin(s):
            return s==s[::-1]
        res=[]
        def backtrack(s,st=0,cur=None):
            if st>=len(s):
                res.append(cur[:])
                return
            if cur==None:
                cur=[]
            for i in range(st+1,len(s)+1):
                a=s[st:i]
                if ispalin(a):
                    cur.append(a)
                    backtrack(s,i,cur)
                    cur.pop()
        backtrack(s)
        return res
```

</details>
