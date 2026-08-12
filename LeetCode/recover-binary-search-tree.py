# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        res=[]
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        res.sort()
        i=0
        def createtree(root):
            nonlocal i
            if root:
                createtree(root.left)
                root.val=res[i]
                i+=1
                createtree(root.right)
        createtree(root)
        """
        Do not return anything, modify root in-place instead.
        """
        