# 🟠 is-graph-bipartite — Is Graph Bipartite?

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/is-graph-bipartite/) &nbsp;|&nbsp; **Solved:** 2026-08-11

---

## 📝 Summary

Determine if an undirected graph can be divided into two independent sets such that every edge connects a vertex in one set to a vertex in the other.

## 🔍 Key Observation

A graph is bipartite if and only if it can be 2-colored such that no two adjacent vertices share the same color.

## ⚙️ Algorithm

**BFS graph coloring**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(V + E)` | `O(V)` |

## 🏷️ Tags

`graph` `bfs` `bipartite` `graph-coloring`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] != -1:
                continue

            color[i] = 0
            queue = [i]
            front = 0

            while front < len(queue):
                node = queue[front]
                front += 1

                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False

        return True
```

</details>
