# 🟠 balanced-binary-tree — Balanced Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/balanced-binary-tree/) &nbsp;|&nbsp; **Solved:** 2025-12-16

---

## 📝 Summary

Accepted solution for Balanced Binary Tree on LeetCode.

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
    def hei(self,root):
            if not root:
                return 0
            return 1+max(self.hei(root.left),self.hei(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        lh=self.hei(root.left)
        rh=self.hei(root.right)
        if abs(lh-rh)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
```

</details>
