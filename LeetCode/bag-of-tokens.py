class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l,r,s,m=0,len(tokens)-1,0,0
        while l<=r:
            if power>=tokens[l]:
                power-=tokens[l]
                s+=1
                l+=1
                m=max(s,m)
            elif s>=1 and l<r:
                power+=tokens[r]
                s-=1
                r-=1
            else:
                break
        return m