class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        cnt1,cnt2=0,0
        ele1,ele2=float('-inf'),float('-inf')
        for i in nums:
            if cnt1==0 and ele2!=i:
                cnt1=1
                ele1=i
            elif cnt2==0 and ele1!=i:
                cnt2=1
                ele2=i
            elif i==ele1:
                cnt1+=1
            elif i==ele2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1=cnt2=0
        for i in nums:
            if i==ele1:
                cnt1+=1
            elif i==ele2:
                cnt2+=1
        res=[]
        if cnt1>n//3:
            res.append(ele1)
        if cnt2>n//3:
            res.append(ele2)
        return res