class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c,e=edges[0]
        cf=ef=True
        for i in range(1,len(edges)):
            if c not in edges[i]:
                cf=False
            if e not in edges[i]:
                ef=False
        return c if cf else e