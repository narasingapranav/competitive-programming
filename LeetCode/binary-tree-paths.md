# 🟠 binary-tree-paths — Binary Tree Paths

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-tree-paths/) &nbsp;|&nbsp; **Solved:** 2026-01-03

---

## 📝 Summary

Accepted solution for Binary Tree Paths on LeetCode.

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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        def dfs(node,path):
            if not node:
                return
            path+=str(node.val)
            if not node.left and not node.right:
                res.append(path)
                return
            path+="->"
            dfs(node.left,path)
            dfs(node.right,path)
        dfs(root,"")
        return res
```

</details>
