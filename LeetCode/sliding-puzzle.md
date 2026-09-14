# 🟠 sliding-puzzle — Sliding Puzzle

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sliding-puzzle/) &nbsp;|&nbsp; **Solved:** 2025-10-11

---

## 📝 Summary

Accepted solution for Sliding Puzzle on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS) + Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`graph` `hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = tuple(num for row in board for num in row)
        goal = (1,2,3,4,5,0)
        neighbors = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[1,3,5],5:[2,4]}
        
        queue = deque([(start,0)])
        visited = set()
        
        while queue:
            state, moves = queue.popleft()
            if state == goal:
                return moves
            if state in visited:
                continue
            visited.add(state)
            zero = state.index(0)
            for n in neighbors[zero]:
                lst = list(state)
                lst[zero], lst[n] = lst[n], lst[zero]
                queue.append((tuple(lst), moves+1))
        return -1        
```

</details>
