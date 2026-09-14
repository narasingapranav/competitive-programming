# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(n,l,h):
            if not n:
                return True
            if not l<n.val<h:
                return False
            return dfs(n.left,l,n.val) and dfs(n.right,n.val,h)
        return dfs(root,float('-inf'),float('inf'))