from typing import List
from collections import Counter
from math import sqrt

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums2)
        B = int(sqrt(n)) + 1
        
        cnt1 = Counter(nums1)
        arr = nums2[:]
        
        blocks = []
        lazy = []
        
        for i in range(0, n, B):
            blocks.append(Counter(arr[i:i+B]))
            lazy.append(0)
        
        def rebuild(b):
            start = b * B
            end = min(n, start + B)
            blocks[b] = Counter(arr[start:end])
        
        ans = []
        
        for q in queries:
            if q[0] == 1:
                _, x, y, val = q
                b1, b2 = x // B, y // B
                
                if b1 == b2:
                    for i in range(x, y + 1):
                        arr[i] += val
                    rebuild(b1)
                else:
                    end1 = min(n, (b1 + 1) * B)
                    for i in range(x, end1):
                        arr[i] += val
                    rebuild(b1)
                    
                    for b in range(b1 + 1, b2):
                        lazy[b] += val
                    
                    start2 = b2 * B
                    for i in range(start2, y + 1):
                        arr[i] += val
                    rebuild(b2)
            
            else:
                _, tot = q
                count = 0
                
                for b in range(len(blocks)):
                    add = lazy[b]
                    for a, c1 in cnt1.items():
                        need = tot - a - add
                        count += c1 * blocks[b].get(need, 0)
                
                ans.append(count)
        
        return ans