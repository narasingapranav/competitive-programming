# 🟠 smallest-string-with-swaps — Smallest String With Swaps

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-string-with-swaps/) &nbsp;|&nbsp; **Solved:** 2026-08-11

---

## 📝 Summary

Given a string and a list of index pairs that can be swapped, find the lexicographically smallest string obtainable through any number of swaps.

## 🔍 Key Observation

Swap operations define connected components of indices; characters in the same connected component can be freely rearranged into sorted order independently of other components.

## ⚙️ Algorithm

**Disjoint Set Union (DSU) + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N log N + M α(N))` | `O(N)` |

## 🏷️ Tags

`dsu` `union-find` `sorting` `string` `graph`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)
		
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])

        return self.parent[a]
        
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
		# 1. Union-Find
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.union(a, b)

		# 2. Grouping
        group = defaultdict(lambda: ([], []))  
        for i, ch in enumerate(s):
            parent = self.find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)

		# 3. Sorting
        res = [''] * len(s)
        for ids, chars in group.values():
            ids.sort()
            chars.sort()
            for ch, i in zip(chars, ids):
                res[i] = ch
                
        return ''.join(res)
```

</details>
