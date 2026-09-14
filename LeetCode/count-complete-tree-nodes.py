# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def l(n):
            h=0
            while n:
                h+=1
                n=n.left
            return h
        def r(n):
            h=0
            while n:
                h+=1
                n=n.right
            return h
        left=l(root)    
        right=r(root)
        if left==right:
            return  (1<<left)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)