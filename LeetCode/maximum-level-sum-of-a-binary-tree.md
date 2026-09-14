# 🟠 maximum-level-sum-of-a-binary-tree — Maximum Level Sum of a Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) &nbsp;|&nbsp; **Solved:** 2026-01-06

---

## 📝 Summary

Accepted solution for Maximum Level Sum of a Binary Tree on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```python
from collections import deque
from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 1
        max_sum = float('-inf')
        ans_level = 1
        while q:
            curr_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if curr_sum > max_sum:
                max_sum = curr_sum
                ans_level = level
            level += 1
        return ans_level

```

</details>
