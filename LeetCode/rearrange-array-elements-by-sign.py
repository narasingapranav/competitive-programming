class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        a=[]
        for i,j in zip(range(len(p)),range(len(n))):
            a.append(p[i])
            a.append(n[j])
        return a