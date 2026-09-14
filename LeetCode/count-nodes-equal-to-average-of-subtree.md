# 🟠 count-nodes-equal-to-average-of-subtree — Count Nodes Equal to Average of Subtree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/) &nbsp;|&nbsp; **Solved:** 2026-09-10

---

## 📝 Summary

Count the number of nodes in a binary tree whose value is equal to the average of the values in its subtree (rounded down).

## 🔍 Key Observation

Using a post-order traversal, each subtree can return its total sum, node count, and valid node count to its parent, enabling the parent to evaluate its condition in O(1) time.

## ⚙️ Algorithm

**Post-order Traversal (DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(h)` |

## 🏷️ Tags

`tree` `depth-first search` `binary tree`

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
            ans=0
            left=self.sumofsubtree(root.left)
            right=self.sumofsubtree(root.right)
            t=root.val+left[0]+right[0]
            ans=left[2]+right[2]
            c+=1+left[1]+right[1]
            if t//c==root.val:
                ans+=1
            return (t,c,ans)
        return (0,0,0)
    def averageOfSubtree(self, root: TreeNode) -> int:
        total,count,ans=self.sumofsubtree(root)
        return ans
```

</details>
