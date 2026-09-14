# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(a):
            if not a:
                return []
            else:
                dfs(a.left)
                res.append(a.val)
                dfs(a.right)
        dfs(root)
        return res
