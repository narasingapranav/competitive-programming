class Solution:
    def jump(self, nums: List[int]) -> int: # [2,3,1,1,4]
        jumps=0 
        curEnd=0
        far=0
        n=len(nums)  # 5
        for i in range(n-1): #           0 | 1     | 2     | 3
            far=max(far,i+nums[i]) #     2 |     4 | 4     | 4
            if i==curEnd: #           true | false | true  | false
                jumps+=1 #               1 | skip  | 2     | skip
                curEnd=far #             2 | skip  | 4     | skip
        return jumps