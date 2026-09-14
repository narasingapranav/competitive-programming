class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s=set()
        n=len(digits)
        for i in range(n):
            if digits[i]==0:
                continue
            for j in range(n):
                if i==j:
                    continue 
                for k in range(n):
                    if k==i or k==j:
                        continue 
                    if digits[k]%2==0:
                        a=digits[i]*100+digits[j]*10+digits[k]
                        s.add(a)
        return len(s)