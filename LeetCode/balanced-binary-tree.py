# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hei(self,root):
            if not root:
                return 0
            return 1+max(self.hei(root.left),self.hei(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        lh=self.hei(root.left)
        rh=self.hei(root.right)
        if abs(lh-rh)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False