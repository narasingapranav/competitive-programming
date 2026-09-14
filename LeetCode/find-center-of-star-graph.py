class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nf=set(edges[0])
        ns=set(edges[1])
        return nf.intersection(ns).pop()