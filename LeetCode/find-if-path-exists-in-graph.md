# 🟠 find-if-path-exists-in-graph — Find if Path Exists in Graph

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-if-path-exists-in-graph/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Given an undirected graph with n vertices and a list of edges, determine if a valid path exists from a source vertex to a destination vertex.

## 🔍 Key Observation

The reachability between two nodes in an unweighted graph can be determined by exploring all connected nodes starting from the source using standard graph traversal.

## ⚙️ Algorithm

**Breadth-First Search**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(V + E)` | `O(V + E)` |

## 🏷️ Tags

`graph` `bfs` `breadth-first-search`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q=deque([source])
        vis=set([source])
        while q:
            node=q.popleft()
            if node == destination:
                    return True
            for nei in graph[node]:
                if nei not in vis:
                    vis.add(nei)
                    q.append(nei)
        return False
```

</details>
