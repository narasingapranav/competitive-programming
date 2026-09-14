class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        d[0]=1
        presum=0
        counter=0
        for e in nums:
            presum+=e
            temp=presum-k
            if temp in d:
                counter+=d[temp]
            d[presum]=d.get(presum,0)+1
        return counter