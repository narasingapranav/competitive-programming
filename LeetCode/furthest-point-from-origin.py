class Solution:
    def furthestDistanceFromOrigin(self, m: str) -> int:
        d=Counter(m)
        maxdist=abs(d['L']-d['R'])+d['_']
        return maxdist