# 🟠 univalued-binary-tree — Univalued Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/univalued-binary-tree/) &nbsp;|&nbsp; **Solved:** 2026-05-18

---

## 📝 Summary

Accepted solution for Univalued Binary Tree on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = deque([root])
        while queue:
            curr_len = len(queue)
            for _ in range(curr_len):
                node = queue.popleft()
                if node.val != root.val:
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return True
```

</details>
