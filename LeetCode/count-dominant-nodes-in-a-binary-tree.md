# 🟠 count-dominant-nodes-in-a-binary-tree — Count Dominant Nodes in a Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/) &nbsp;|&nbsp; **Solved:** 2026-07-19

---

## 📝 Summary

Accepted solution for Count Dominant Nodes in a Binary Tree on LeetCode.

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
    def countDominantNodes(self, root: TreeNode | None) -> int:
        leaf=0
        def countleaf(root):
            if not root:
                return 0
            if not root.right and not root.left:
                return 1
            lt=countleaf(root.left)
            rt= countleaf(root.right)
            return lt+rt
        def finddom(root):
            if not root:
                return (float('-inf'),0)
            leftmax,leftcount=finddom(root.left)
            rightmax,rightcount=finddom(root.right)
            m=max(leftmax,rightmax,root.val)
            count=leftcount+rightcount
            if( root.left or root.right )and root.val==m:
                count+=1
            return (m,count)
        m,cnt=finddom(root)
        return cnt+countleaf(root)
```

</details>
