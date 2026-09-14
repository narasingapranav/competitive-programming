# 🟠 balance-a-binary-search-tree — Balance a Binary Search Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/balance-a-binary-search-tree/) &nbsp;|&nbsp; **Solved:** 2026-02-09

---

## 📝 Summary

Accepted solution for Balance a Binary Search Tree on LeetCode.

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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        
        inorder(root)
        def buildBalancedBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nodes[mid])
            root.left = buildBalancedBST(left, mid - 1)
            root.right = buildBalancedBST(mid + 1, right)
            return root
        
        return buildBalancedBST(0, len(nodes) - 1)
```

</details>
