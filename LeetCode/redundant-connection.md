# 🟠 redundant-connection — Redundant Connection

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/redundant-connection/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Given an undirected graph with $n$ nodes and $n$ edges that forms a tree with one extra cycle-creating edge, find and return the last edge in the input list that creates a cycle.

## 🔍 Key Observation

The redundant edge connects two vertices that are already part of the same connected component.

## ⚙️ Algorithm

**Disjoint Set Union (Union-Find)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n \alpha(n))` | `O(n)` |

## 🏷️ Tags

`graph` `union-find` `tree` `cycle-detection`

<details>
<summary>💻 View solution</summary>

```python
class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
    def find(self,x):
        if x==self.parent[x]:
            return x
        return self.find(self.parent[x])
    def union(self,x,y):
        pa=self.find(x)
        pb=self.find(y)
        if pa!=pb:
            self.parent[pb]=pa
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=max(max(u,v) for u,v in edges)+1
        uf=UnionFind(n)
        res=[]
        for u,v in edges:
            if uf.find(v)==uf.find(u):
                return [u,v]
            uf.union(u,v)
```

</details>
