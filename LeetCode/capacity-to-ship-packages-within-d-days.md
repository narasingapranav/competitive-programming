# 🟠 capacity-to-ship-packages-within-d-days — Capacity To Ship Packages Within D Days

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) &nbsp;|&nbsp; **Solved:** 2026-08-11

---

## 📝 Summary

Determine the minimum weight capacity of a ship required to convey all packages in their given order within a specified number of days.

## 🔍 Key Observation

The feasibility of shipping packages within $D$ days is monotonic with respect to ship capacity, allowing binary search over the search space bounded by the maximum package weight and the total sum of weights.

## ⚙️ Algorithm

**Binary Search on Answer + Greedy Validation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * log(sum(weights) - max(weights)))` | `O(1)` |

## 🏷️ Tags

`binary-search` `greedy` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def solve(wei):
            total=1
            w=0
            for i in weights:
                if w+i>wei:
                    total+=1
                    w=i
                else:
                    w+=i
            return total
        l=max(weights)
        h=sum(weights)
        while l<=h:
            mid=l+(h-l)//2
            if solve(mid)>days:
                l=mid+1
            else:
                h=mid-1
        return l
```

</details>
