class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarrays=[]
        for i in range(0,len(nums)-k+1):
            subarrays.append(nums[i:i+k])
        c={}
        for i in subarrays:
            for j in (set(i)):
                c[j]=c.get(j,0)+1
        res=[]
        for i in c:
            if c[i]==1:
                res.append(i)
        return max(res) if res else -1