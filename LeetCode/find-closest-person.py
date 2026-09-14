class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xz=abs(x-z)
        yz=abs(y-z)
        if xz==yz:
            return 0
        return 2 if xz>yz else 1