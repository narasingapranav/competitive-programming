# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        leaf=0
        def countleaf(root):
            if not root:
                return 0
            if not root.right and not root.left:
                return 1
            lt=countleaf(root.left)
            rt= countleaf(root.right)
            return lt+rt
        def finddom(root):
            if not root:
                return (float('-inf'),0)
            leftmax,leftcount=finddom(root.left)
            rightmax,rightcount=finddom(root.right)
            m=max(leftmax,rightmax,root.val)
            count=leftcount+rightcount
            if( root.left or root.right )and root.val==m:
                count+=1
            return (m,count)
        m,cnt=finddom(root)
        return cnt+countleaf(root)