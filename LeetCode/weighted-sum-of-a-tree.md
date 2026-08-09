# 🟠 weighted-sum-of-a-tree — Weighted Sum of a Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/weighted-sum-of-a-tree/) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Given a tree represented by a parent array and an array of node values, calculate the weighted sum of node values where each node's weight is determined by its distance from the tree's maximum depth.

## 🔍 Key Observation

By computing the depth of every node using memoized parent traversal, we can determine the maximum height of the tree and evaluate each node's weight factor in linear time.

## ⚙️ Algorithm

**Memoized Recursion / Tree Traversal**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`tree` `dfs` `memoization` `recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n=len(parent)
        depth=[0]*n
        depth[0]=1
        ans=0
        h=1
        def findlevel(node):
            if parent[node]==-1:
                return 1
            if depth[node]!=0:
                return depth[node]
            depth[node]=findlevel(parent[node])+1
            return depth[node]
        for i in range(n):
            if depth[i]==0:
                findlevel(i)
            h=max(h,depth[i])
        for i in range(n):
            ans+=nums[i]*(h-depth[i]+1)
        return ans
```

</details>
