# 🟠 serialize-and-deserialize-binary-tree — Serialize and Deserialize Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Accepted solution for Serialize and Deserialize Binary Tree on LeetCode.

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
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def makestr(self,node):
        if node is None:
            self.l.append("N")
            return

        self.l.append(str(node.val))
        self.makestr(node.left)
        self.makestr(node.right)

    def build(self):
        if self.i>=len(self.data):
            return None
        a=self.data[self.i]
        if a=="N":
            self.i+=1
            return None
        n=TreeNode(a)
        self.i+=1
        n.left=self.build()
        n.right=self.build()
        return n
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.l=[]
        self.makestr(root)
        return ",".join(self.l)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i=0
        self.data=data.split(",")
        root=self.build()
        return root
            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```

</details>
