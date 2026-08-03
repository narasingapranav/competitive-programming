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