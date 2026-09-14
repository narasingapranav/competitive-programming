# 🟠 convert-sorted-array-to-binary-search-tree — Convert Sorted Array to Binary Search Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) &nbsp;|&nbsp; **Solved:** 2026-07-06

---

## 📝 Summary

Accepted solution for Convert Sorted Array to Binary Search Tree on LeetCode.

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
    def sortedArrayToBST(self, l: List[int]) -> Optional[TreeNode]:
        if not l:
            return None
        mid=len(l)//2
        root=TreeNode(l[mid])
        root.left=self.sortedArrayToBST(l[:mid])
        root.right=self.sortedArrayToBST(l[mid+1:])
        return root
        

```

</details>
