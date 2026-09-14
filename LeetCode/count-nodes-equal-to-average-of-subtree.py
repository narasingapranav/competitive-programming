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
            ans=0
            left=self.sumofsubtree(root.left)
            right=self.sumofsubtree(root.right)
            t=root.val+left[0]+right[0]
            ans=left[2]+right[2]
            c+=1+left[1]+right[1]
            if t//c==root.val:
                ans+=1
            return (t,c,ans)
        return (0,0,0)
    def averageOfSubtree(self, root: TreeNode) -> int:
        total,count,ans=self.sumofsubtree(root)
        return ans