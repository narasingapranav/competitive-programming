# 🟠 kth-smallest-element-in-a-bst — Kth Smallest Element in a BST

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) &nbsp;|&nbsp; **Solved:** 2025-12-16

---

## 📝 Summary

Accepted solution for Kth Smallest Element in a BST on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s=[]
        cur=root
        while True :
            while cur:
                s.append(cur)
                cur=cur.left
            cur=s.pop()
            k-=1
            if k==0:
                return cur.val
            cur=cur.right
```

</details>
