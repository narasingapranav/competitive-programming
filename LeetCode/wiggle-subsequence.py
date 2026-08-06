class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        s1=1
        s2=1
        s1prev=nums[0]
        s2prev=nums[0]
        t1=1
        t2=-1
        for i in range(1,len(nums)):
            if nums[i]>s1prev:
                if t1==1:
                    s1prev=nums[i]
                    s1+=1
                    t1=-1
                else:
                    s1prev=max(s1prev,nums[i])
            elif nums[i]<s1prev:
                if t1==-1:
                    s1prev=nums[i]
                    s1+=1
                    t1=1
                else:
                    s1prev=min(s1prev,nums[i])
            if nums[i]>s2prev:
                if t2==1:
                    s2prev=nums[i]
                    s2+=1
                    t2=-1
                else:
                    s2prev=max(s2prev,nums[i])
            elif nums[i]<s2prev:
                if t2==-1:
                    s2prev=nums[i]
                    s2+=1
                    t2=1
                else:
                    s2prev=min(s2prev,nums[i])
        return max(s1,s2)