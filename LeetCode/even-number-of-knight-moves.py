class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return (start[1]+start[0])%2==(target[0]+target[1])%2