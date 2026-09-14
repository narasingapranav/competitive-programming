# 🟠 count-nodes-equal-to-average-of-subtree — Count Nodes Equal to Average of Subtree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/) &nbsp;|&nbsp; **Solved:** 2026-09-10

---

## 📝 Summary

Count the number of nodes in a binary tree where the node's value equals the floor-divided average of all values in its subtree.

## 🔍 Key Observation

A post-order traversal allows each node to calculate its subtree's total sum and node count in O(1) time by aggregating results from its left and right children.

## ⚙️ Algorithm

**Post-order DFS**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(h)` |

## 🏷️ Tags

`binary-tree` `dfs` `tree`

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
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return (0,0,0)
            left=dfs(root.left)
            right=dfs(root.right)
            t=root.val+left[0]+right[0]
            c=1+left[1]+right[1]
            ans=left[2]+right[2]
            if t//c==root.val:
                ans+=1
            return (t,c,ans)
        return dfs(root)[2]
```

</details>
