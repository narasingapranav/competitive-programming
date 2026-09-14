# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=[root]
        a=[]
        while q:
            l=[]
            s=len(q)
            for i in range(s):
                n=q.pop(0)
                l.append(n.val)
                if n.left:
                    q.append(n.left)    
                if n.right:
                    q.append(n.right)
            a.append(l)
        return a