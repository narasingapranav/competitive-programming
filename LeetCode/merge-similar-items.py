class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        for v, w in items1 + items2:
            d[v] = d.get(v, 0) + w
        return [[v, d[v]] for v in sorted(d)]
