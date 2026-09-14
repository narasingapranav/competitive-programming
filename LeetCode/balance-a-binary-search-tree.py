# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        
        inorder(root)
        def buildBalancedBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nodes[mid])
            root.left = buildBalancedBST(left, mid - 1)
            root.right = buildBalancedBST(mid + 1, right)
            return root
        
        return buildBalancedBST(0, len(nodes) - 1)