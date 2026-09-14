# 🟠 binary-search-tree-iterator — Binary Search Tree Iterator

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-search-tree-iterator/) &nbsp;|&nbsp; **Solved:** 2026-07-07

---

## 📝 Summary

Accepted solution for Binary Search Tree Iterator on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion + Two pointers**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.a=[]
        self.i=0
        self.inorder(root)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.a.append(root.val)
            self.inorder(root.right)

    def next(self) -> int:
       res=self.a[self.i]
       self.i+=1
       return res

    def hasNext(self) -> bool:
        return self.i<len(self.a)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

</details>
