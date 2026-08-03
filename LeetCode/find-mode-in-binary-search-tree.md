# 🟠 find-mode-in-binary-search-tree — Find Mode in Binary Search Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-mode-in-binary-search-tree/) &nbsp;|&nbsp; **Solved:** 2026-08-03

---

## 📝 Summary

Find all modes (most frequently occurring values) in a Binary Search Tree (BST).

## 🔍 Key Observation

Performing an in-order traversal collects all node values, after which a frequency count map can easily identify the values with the maximum occurrence.

## ⚙️ Algorithm

**In-order traversal + Hash Map**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(N)` |

## 🏷️ Tags

`tree` `binary-search-tree` `depth-first-search` `hash-table`

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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        d = {}
        for x in res:
            d[x] = d.get(x, 0) + 1
        mx = max(d.values())
        ans = []
        for key, value in d.items():
            if value == mx:
                ans.append(key)
        return ans
```

</details>
