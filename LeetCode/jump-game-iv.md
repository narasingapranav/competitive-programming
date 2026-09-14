# 🟠 jump-game-iv — Jump Game IV

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/jump-game-iv/) &nbsp;|&nbsp; **Solved:** 2026-05-18

---

## 📝 Summary

Accepted solution for Jump Game IV on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
  def minJumps(self, arr: List[int]) -> int:
    n = len(arr)
    graph = collections.defaultdict(list)
    steps = 0
    q = collections.deque([0])
    seen = {0}
    for i, a in enumerate(arr):
      graph[a].append(i)
    while q:
      for _ in range(len(q)):
        i = q.popleft()
        if i == n - 1:
          return steps
        seen.add(i)
        u = arr[i]
        if i + 1 < n:
          graph[u].append(i + 1)
        if i - 1 >= 0:
          graph[u].append(i - 1)
        for v in graph[u]:
          if v in seen:
            continue
          q.append(v)
        graph[u].clear()
      steps += 1
```

</details>
