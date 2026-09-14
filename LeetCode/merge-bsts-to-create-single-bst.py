# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Input  : [[2,1],[3,2,5],[5,4]]
        Output : [3,2,5,1,null,4]
    '''
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        rootDict={}
        countFreq={}
        for t in trees:
            rootDict[t.val]=t
            countFreq[t.val]=countFreq.get(t.val,0)+1
            if t.left:
                countFreq[t.left.val]=countFreq.get(t.left.val,0)+1
            
            if t.right:
                countFreq[t.right.val]=countFreq.get(t.right.val,0)+1

        root=None
        for t in trees:
            if countFreq[t.val]==1:
                root=t
                break
        if not root:
            return None

        # DFS + BST(Correct)
        def DFS(node,low,high):
            if not node:
                return True

            if not (low<node.val<high):
                return False
            if not node.left and not node.right and node.val in rootDict:
                m=rootDict[node.val]
                if m!=node:
                    node.left=m.left
                    node.right=m.right
                    del rootDict[node.val]
            return DFS(node.left,low,node.val) and DFS(node.right,node.val,high)
        if DFS(root,float("-inf"),float("inf")) and len(rootDict)==1:
            return root
        return None
            