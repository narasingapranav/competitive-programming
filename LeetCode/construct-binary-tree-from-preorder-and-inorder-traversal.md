# 🟠 construct-binary-tree-from-preorder-and-inorder-traversal — Construct Binary Tree from Preorder and Inorder Traversal

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) &nbsp;|&nbsp; **Solved:** 2025-12-17

---

## 📝 Summary

Accepted solution for Construct Binary Tree from Preorder and Inorder Traversal on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Two pointers**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ind=inorder.index(preorder.pop(0))
            root=TreeNode(inorder[ind])
            root.left=self.buildTree(preorder,inorder[:ind])
            root.right=self.buildTree(preorder,inorder[ind+1:])
            return root
```

</details>
