# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = [] 
        if not root:
            return levels
        queue = collections.deque([root])
        while queue:
            level_length = len(queue)
            curr_level = []
            for i in range(level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                curr_level.append(node.val)
            levels.append(curr_level)
        return levels
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        l=self.levelOrder(root)
        ans=[]
        for i in l:
            ans.append(sum(i)/len(i))
        return ans