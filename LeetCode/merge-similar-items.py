class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d={}
        for i in items1:
            if i[0] not in d:
                d[i[0]]=i[1]
        for i in items2:
            if i[0] not in d:
                d[i[0]]=i[1]
            else:
                d[i[0]]+=i[1]
        l=[]
        for i in d:
            l.append([i,d[i]])
        l.sort(key=lambda x:x[0])
        return l