class Solution:
    def maximizeSquareArea(
        self,
        m: int,
        n: int,
        hFences: List[int],
        vFences: List[int],
    ) -> int:
        MOD = 10**9+7
        
        # add boundaries
        hF = [1] + sorted(hFences) + [m]
        vF = [1] + sorted(vFences) + [n]
        
        # compute all horizontal distances
        hGaps = {hF[j] - hF[i] for i in range(len(hF)) for j in range(i+1, len(hF))}
        
        # compute all vertical distances
        vGaps = {vF[j] - vF[i] for i in range(len(vF)) for j in range(i+1, len(vF))}
        
        # find common distances
        common = hGaps & vGaps
        
        if not common:
            return -1
        
        max_side = max(common)
        return (max_side * max_side) % MOD