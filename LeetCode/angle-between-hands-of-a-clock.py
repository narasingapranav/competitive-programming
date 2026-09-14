class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        t=abs(30*hour - 5.5*minutes)
        if t >180:
            return 360-t
        return t