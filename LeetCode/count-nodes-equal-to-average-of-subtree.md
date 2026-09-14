# 🟠 count-nodes-equal-to-average-of-subtree — Count Nodes Equal to Average of Subtree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/) &nbsp;|&nbsp; **Solved:** 2026-09-10

---

## 📝 Summary

Count the number of nodes in a binary tree whose value is equal to the average of all values in their subtree, rounded down.

## 🔍 Key Observation

A subtree's sum and node count can be computed recursively from the sum and node count of its left and right subtrees.

## ⚙️ Algorithm

**Depth-first search (DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n)` |

## 🏷️ Tags

`tree` `depth-first-search` `binary-tree`

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
    def sumofsubtree(self,root):
        if root:
            c=0
            t=0
            left=self.sumofsubtree(root.left)
            right=self.sumofsubtree(root.right)
            t=root.val+left[0]+right[0]
            c+=1+left[1]+right[1]
            return (t,c)
        return (0,0)
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans=0
        if root:
            total,count=self.sumofsubtree(root)
            if total//count==root.val:
                ans+=1
            left=self.averageOfSubtree(root.left)
            right=self.averageOfSubtree(root.right)
            ans+=left+right
        return ans
```

</details>
