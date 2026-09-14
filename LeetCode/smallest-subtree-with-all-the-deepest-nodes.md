# 🟠 smallest-subtree-with-all-the-deepest-nodes — Smallest Subtree with all the Deepest Nodes

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) &nbsp;|&nbsp; **Solved:** 2026-01-09

---

## 📝 Summary

Accepted solution for Smallest Subtree with all the Deepest Nodes on LeetCode.

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
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return 0, None

            ld, ln = dfs(node.left)
            rd, rn = dfs(node.right)

            if ld > rd:
                return ld + 1, ln
            if rd > ld:
                return rd + 1, rn

            return ld + 1, node  # both sides same depth

        return dfs(root)[1]
```

</details>
