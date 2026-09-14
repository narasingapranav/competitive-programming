# 🟠 binary-tree-maximum-path-sum — Binary Tree Maximum Path Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Accepted solution for Binary Tree Maximum Path Sum on LeetCode.

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxi=float('-inf')
        def dfs(node):
            lg,rg=0,0
            if node.left is not None:
                lg=max(dfs(node.left),0)
            if node.right is not None:
                rg=max(dfs(node.right),0)
            ans=lg+rg+node.val
            self.maxi=max(self.maxi,ans)
            return node.val+max(lg,rg)
        dfs(root)
        return self.maxi
```

</details>
