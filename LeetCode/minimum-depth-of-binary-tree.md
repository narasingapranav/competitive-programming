# 🟠 minimum-depth-of-binary-tree — Minimum Depth of Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/) &nbsp;|&nbsp; **Solved:** 2025-12-03

---

## 📝 Summary

Accepted solution for Minimum Depth of Binary Tree on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS) + Two pointers**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([(root,1)])
        while q:
            node,length=q.popleft()
            if not node.left and not node.right:
                return length
            if node.left:
                q.append((node.left,length+1))
            if node.right:
                q.append((node.right,length+1))
```

</details>
