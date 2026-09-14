# 🟠 merge-similar-items — Merge Similar Items

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/merge-similar-items/) &nbsp;|&nbsp; **Solved:** 2026-01-01

---

## 📝 Summary

Accepted solution for Merge Similar Items on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d={}
        for i in items1:
            if i[0] not in d:
                d[i[0]]=i[1]
        for i in items2:
            if i[0] not in d:
                d[i[0]]=i[1]
            else:
                d[i[0]]+=i[1]
        l=[]
        for i in d:
            l.append([i,d[i]])
        l.sort(key=lambda x:x[0])
        return l
```

</details>
