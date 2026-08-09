class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n=len(parent)
        depth=[0]*n
        depth[0]=1
        ans=0
        h=1
        def findlevel(node):
            if parent[node]==-1:
                return 1
            if depth[node]!=0:
                return depth[node]
            depth[node]=findlevel(parent[node])+1
            return depth[node]
        for i in range(n):
            if depth[i]==0:
                findlevel(i)
            h=max(h,depth[i])
        for i in range(n):
            ans+=nums[i]*(h-depth[i]+1)
        return ans