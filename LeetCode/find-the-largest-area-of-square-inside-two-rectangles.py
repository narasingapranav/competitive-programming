from typing import List
import itertools

class Solution:
    def largestSquareArea(
        self,
        bottomLeft: List[List[int]],
        topRight: List[List[int]],
    ) -> int:
        max_area = 0
        
        
        for (x1, y1), (x2, y2), (x3, y3), (x4, y4) in (
            ((bl1[0], bl1[1]), (tr1[0], tr1[1]),
             (bl2[0], bl2[1]), (tr2[0], tr2[1]))
            for (bl1, tr1), (bl2, tr2) in itertools.combinations(zip(bottomLeft, topRight), 2)
        ):
            
            overlap_width = min(x2, x4) - max(x1, x3)
            overlap_height = min(y2, y4) - max(y1, y3)
            
            if overlap_width > 0 and overlap_height > 0:
                side = min(overlap_width, overlap_height)
                max_area = max(max_area, side * side)
        
        return max_area