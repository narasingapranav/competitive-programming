# 🟠 maximum-binary-tree — Maximum Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-binary-tree/) &nbsp;|&nbsp; **Solved:** 2026-08-12

---

## 📝 Summary

Given an integer array with unique values, construct a maximum binary tree where the root is the maximum value, and its left and right subtrees are built recursively from the prefix and suffix subarrays.

## 🔍 Key Observation

A monotonic decreasing stack can construct the tree in linear time: each new node pops smaller nodes from the stack to set as its left subtree, and then attaches itself as the right child of the nearest larger element remaining on the stack.

## ⚙️ Algorithm

**Monotonic stack**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`tree` `binary-tree` `stack` `monotonic-stack`

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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            curr = TreeNode(num)
            while stack and stack[-1].val < num:
                curr.left = stack.pop()
            if stack:
                stack[-1].right = curr
            stack.append(curr)
        return stack[0]
```

</details>
