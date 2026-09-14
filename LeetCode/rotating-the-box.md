# 🟠 rotating-the-box — Rotating the Box

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rotating-the-box/) &nbsp;|&nbsp; **Solved:** 2026-05-06

---

## 📝 Summary

Accepted solution for Rotating the Box on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def rotateTheBox(self, box):
        rows = len(box)
        cols = len(box[0])
        for r in range(rows):
            empty = cols - 1
            for c in range(cols - 1, -1, -1):
                if box[r][c] == '*':
                    empty = c - 1
                elif box[r][c] == '#':
                    box[r][c], box[r][empty] = \
                    box[r][empty], box[r][c]
                    empty -= 1
        ans = [[0] * rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                ans[c][rows - 1 - r] = box[r][c]
        return ans
```

</details>
