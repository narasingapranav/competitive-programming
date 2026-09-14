# 🟠 sum-of-root-to-leaf-binary-numbers — Sum of Root To Leaf Binary Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Accepted solution for Sum of Root To Leaf Binary Numbers on LeetCode.

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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        tot = 0
        stack = [(root,str(root.val))]
        while stack:
            node, binVal = stack.pop()
            if node.left:
                stack.append((node.left,binVal+str(node.left.val)))
            if node.right:
                stack.append((node.right,binVal+str(node.right.val)))
            if not node.left and not node.right:
                tot += int(binVal,2)
        return tot
```

</details>
