class Solution:
    def furthestDistanceFromOrigin(self, m: str) -> int:
        return (d:=Counter(m)) and (abs(d['L']-d['R'])+d['_'])