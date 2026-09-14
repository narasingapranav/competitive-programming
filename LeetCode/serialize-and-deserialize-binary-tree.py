from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def makestr(self,node):
        if node is None:
            self.l.append("N")
            return

        self.l.append(str(node.val))
        self.makestr(node.left)
        self.makestr(node.right)

    def build(self):
        if self.i>=len(self.data):
            return None
        a=self.data[self.i]
        if a=="N":
            self.i+=1
            return None
        n=TreeNode(a)
        self.i+=1
        n.left=self.build()
        n.right=self.build()
        return n
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.l=[]
        self.makestr(root)
        return ",".join(self.l)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i=0
        self.data=data.split(",")
        root=self.build()
        return root
            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))