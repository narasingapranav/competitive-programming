# 🟠 remove-methods-from-project — Remove Methods From Project

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-methods-from-project/) &nbsp;|&nbsp; **Solved:** 2026-08-05

---

## 📝 Summary

Given a directed graph of method invocations and a starting suspicious method, determine whether the entire component reachable from the starting method can be removed without leaving any dangling invocations from non-suspicious methods.

## 🔍 Key Observation

If any method outside the suspicious component invokes a method inside the suspicious component, no methods can be removed; otherwise, all methods reachable from the starting method can be safely removed.

## ⚙️ Algorithm

**Breadth-First Search (BFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n + m)` | `O(n + m)` |

## 🏷️ Tags

`graph` `bfs` `depth-first search`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        sus=[False]*n
        graph=defaultdict(list)
        for i,j in invocations:
            graph[i].append(j)
        sus[k]=True
        q=deque([k])
        while q:
            no=q.popleft()
            for nei in graph[no]:
                if not sus[nei]:
                    sus[nei]=True
                    q.append(nei)
        for u, v in invocations:
            if not sus[u] and sus[v]:
                return list(range(n))

        return [i for i in range(n) if not sus[i]]
```

</details>
