# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, l: List[int]) -> Optional[TreeNode]:
        if not l:
            return None
        mid=len(l)//2
        root=TreeNode(l[mid])
        root.left=self.sortedArrayToBST(l[:mid])
        root.right=self.sortedArrayToBST(l[mid+1:])
        return root
        
