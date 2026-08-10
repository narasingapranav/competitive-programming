# 🟠 total-cost-to-hire-k-workers — Total Cost to Hire K Workers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/total-cost-to-hire-k-workers/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Select k workers with the minimum total cost by repeatedly choosing the cheapest worker from either the first or last candidates available workers.

## 🔍 Key Observation

Maintaining two min-heaps for the candidate pools at both ends allows efficient retrieval of the global minimum candidate at each step while two pointers refill the heaps.

## ⚙️ Algorithm

**Two Heaps + Two Pointers**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O((k + candidates) log candidates)` | `O(candidates)` |

## 🏷️ Tags

`heap` `priority-queue` `two-pointers` `greedy`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i=0
        j=len(costs)-1
        pq1=[]
        pq2=[]
        ans=0
        while k>0:
            while len(pq1)<candidates and i<=j:
                heapq.heappush(pq1,costs[i])
                i+=1
            while len(pq2)<candidates and i<=j:
                heapq.heappush(pq2,costs[j])
                j-=1   
            t1=pq1[0] if pq1 else float('inf')
            t2=pq2[0] if pq2 else float('inf')
            if t1<=t2:
                ans+=t1
                heapq.heappop(pq1)
            else:
                ans+=t2
                heapq.heappop(pq2)
            k-=1
        return ans
            
```

</details>
