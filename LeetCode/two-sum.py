class Solution:
    def twoSum(self,arr,k):
        l=[(arr[i],i) for i in range(len(arr))]
        l.sort()
        i=0
        j=len(arr)-1
        while i<j:
            if l[i][0]+l[j][0] > k:
                j-=1
            elif l[i][0]+l[j][0] < k:
                i+=1
            else:
                return [l[i][1],l[j][1]]
        return [-1,-1]