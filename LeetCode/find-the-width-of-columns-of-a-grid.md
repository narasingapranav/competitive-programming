# 🟠 find-the-width-of-columns-of-a-grid — Find the Width of Columns of a Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Accepted solution for Find the Width of Columns of a Grid on LeetCode.

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
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        out = []
        for j in range(len(grid[0])):
            maxlen=0
            for i in range(len(grid)):
                if grid[i][j] == 0:
                    maxlen = max(maxlen,1)
                elif grid[i][j]<0:
                    maxlen = max(maxlen,math.floor(math.log10(-grid[i][j]))+2)
                    print(maxlen)
                else:
                    maxlen = max(maxlen,math.floor(math.log10(grid[i][j]))+1)
                    print(maxlen)
            out.append(maxlen)
        return out
```

</details>
