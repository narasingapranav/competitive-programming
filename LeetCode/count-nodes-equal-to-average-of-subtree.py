# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumofsubtree(self,root):
        if root:
            c=0
            t=0
            left=self.sumofsubtree(root.left)
            right=self.sumofsubtree(root.right)
            t=root.val+left[0]+right[0]
            c+=1+left[1]+right[1]
            return (t,c)
        return (0,0)
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans=0
        if root:
            total,count=self.sumofsubtree(root)
            if total//count==root.val:
                ans+=1
            left=self.averageOfSubtree(root.left)
            right=self.averageOfSubtree(root.right)
            if left:
                ans+=left
            if right:
                ans+=right
            return ans