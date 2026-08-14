class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=deque()
        d=deque()
        for i in range(len(senate)):
            if senate[i]=='R':
                r.append(i)
            else:
                d.append(i)
        n=len(senate)
        while r and d:
            if r[0]<d[0]:
                r.append(r.popleft()+n)
                d.popleft()
            else:
                d.append(d.popleft()+n)
                r.popleft()
        if r:
            return "Radiant"
        else:
            return "Dire"