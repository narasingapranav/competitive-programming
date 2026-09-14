# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return (0,0,0)
            left=dfs(root.left)
            right=dfs(root.right)
            t=root.val+left[0]+right[0]
            c=1+left[1]+right[1]
            ans=left[2]+right[2]
            if t//c==root.val:
                ans+=1
            return (t,c,ans)
        return dfs(root)[2]