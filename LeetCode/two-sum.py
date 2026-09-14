class Solution:
    def twoSum(self,arr,k):
        dic={}
        for i , num in enumerate(arr):
            c=k-num
            if c in dic:
                return [dic[c],i]
            dic[num]=i