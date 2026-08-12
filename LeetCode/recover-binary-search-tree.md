# 🟠 recover-binary-search-tree — Recover Binary Search Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/recover-binary-search-tree/) &nbsp;|&nbsp; **Solved:** 2026-08-12

---

## 📝 Summary

You are given a Binary Search Tree where the values of exactly two nodes have been swapped by mistake. The task is to recover the tree without changing its structure.

## 🔍 Key Observation

An in-order traversal of a valid BST produces a strictly increasing sequence of values; collecting all values, sorting them, and reassigning them via a second in-order traversal restores the original BST property.

## ⚙️ Algorithm

**In-order traversal + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N log N)` | `O(N)` |

## 🏷️ Tags

`tree` `binary-search-tree` `depth-first-search` `inorder-traversal`

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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        res=[]
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        res.sort()
        i=0
        def createtree(root):
            nonlocal i
            if root:
                createtree(root.left)
                root.val=res[i]
                i+=1
                createtree(root.right)
        createtree(root)
        """
        Do not return anything, modify root in-place instead.
        """
        
```

</details>
