# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxi=float('-inf')
        def dfs(node):
            lg,rg=0,0
            if node.left is not None:
                lg=max(dfs(node.left),0)
            if node.right is not None:
                rg=max(dfs(node.right),0)
            ans=lg+rg+node.val
            self.maxi=max(self.maxi,ans)
            return node.val+max(lg,rg)
        dfs(root)
        return self.maxi