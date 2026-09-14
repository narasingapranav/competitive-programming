class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m=0
        c=1
        i=0
        while m<k:
            if i<len(arr) and arr[i]==c:
                i+=1
            else:
                m+=1
                if m==k:
                    return c
            c+=1