# 🟠 construct-binary-tree-from-inorder-and-postorder-traversal — Construct Binary Tree from Inorder and Postorder Traversal

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Reconstruct a unique binary tree given its inorder and postorder traversal sequences.

## 🔍 Key Observation

The last element of the postorder sequence is always the root of the current subtree, and finding its position in the inorder sequence divides the elements into left and right subtrees.

## ⚙️ Algorithm

**Divide and conquer / Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n^2)` |

## 🏷️ Tags

`binary-tree` `recursion` `divide-and-conquer` `tree`

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ind=inorder.index(postorder.pop())
            root=TreeNode(inorder[ind])
            root.right=self.buildTree(inorder[ind+1:],postorder)
            root.left=self.buildTree(inorder[:ind],postorder)
            return root
```

</details>
