from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels=[]
        if not root:
            return levels
        q=deque([root])
        while q:
            level_len=len(q)
            prelevel=[]
            for i in range(level_len):
                n=q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                prelevel.append(n.val)
            levels.append(prelevel)
        return levels