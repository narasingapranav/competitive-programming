class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.tree=[0]*(2*self.n)
        for i in range(self.n):
            self.tree[i+self.n]=nums[i]
        for i in range(self.n-1,0,-1):
            self.tree[i]=self.tree[i<<1]+self.tree[i<<1 | 1]

    def update(self, index: int, val: int) -> None:
        i=index+self.n
        self.tree[i]=val
        j=i>>1
        while j>0 :
            self.tree[j]=self.tree[j<<1]+self.tree[j<<1 | 1]
            j>>=1

    def sumRange(self, left: int, right: int) -> int:
        res=0
        l=left+self.n
        r=right+self.n
        while l<=r:
            if l &1:
                res+=self.tree[l]
                l+=1
            if r&1 ==0:
                res+=self.tree[r]
                r-=1
            l>>=1
            r>>=1
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)