# 🟠 average-of-levels-in-binary-tree — Average of Levels in Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/average-of-levels-in-binary-tree/) &nbsp;|&nbsp; **Solved:** 2026-09-07

---

## 📝 Summary

Calculate the average value of the nodes at each level of a given binary tree.

## 🔍 Key Observation

A level-order traversal using BFS allows us to isolate nodes level by level to compute each level's average value.

## ⚙️ Algorithm

**Breadth-First Search (BFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`binary-tree` `bfs` `tree`

<details>
<summary>💻 View solution</summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = [] 
        if not root:
            return levels
        queue = collections.deque([root])
        while queue:
            level_length = len(queue)
            curr_level = []
            for i in range(level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                curr_level.append(node.val)
            levels.append(curr_level)
        return levels
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        l=self.levelOrder(root)
        ans=[]
        for i in l:
            ans.append(sum(i)/len(i))
        return ans
```

</details>
