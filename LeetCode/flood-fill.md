# 🟠 flood-fill — Flood Fill

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/flood-fill/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Accepted solution for Flood Fill on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```python
from collections import deque
from typing import List

class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int
    ) -> List[List[int]]:

        m, n = len(image), len(image[0])

        clr = image[sr][sc]

        if clr == color:
            return image

        q = deque([(sr, sc)])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c = q.popleft()

            image[r][c] = color

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and image[nr][nc] == clr
                ):
                    q.append((nr, nc))

        return image
```

</details>
