# 🟠 maximum-product-of-splitted-binary-tree — Maximum Product of Splitted Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/) &nbsp;|&nbsp; **Solved:** 2026-01-07

---

## 📝 Summary

Accepted solution for Maximum Product of Splitted Binary Tree on LeetCode.

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
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.max_prod = 0
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        total = totalSum(root)
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            sub_sum = node.val + left + right
            self.max_prod = max(self.max_prod, sub_sum * (total - sub_sum))
            return sub_sum
        dfs(root)
        return self.max_prod % MOD
        return self.max_prod % MOD
        
```

</details>
