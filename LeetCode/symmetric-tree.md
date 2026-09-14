# 🟠 symmetric-tree — Symmetric Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/symmetric-tree/) &nbsp;|&nbsp; **Solved:** 2025-09-06

---

## 📝 Summary

Accepted solution for Symmetric Tree on LeetCode.

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mir(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val==t2.val and
                mir(t1.left, t2.right) and
                mir (t1.right,t2.left)
            )
        return(mir(root.left,root.right))
```

</details>
