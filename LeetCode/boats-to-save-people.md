# 🟠 boats-to-save-people — Boats to Save People

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/boats-to-save-people/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Given an array representing the weights of people and a weight limit for each boat, find the minimum number of boats needed to rescue everyone, where each boat carries at most two people whose combined weight does not exceed the limit.

## 🔍 Key Observation

To minimize the total boats, always pair the heaviest remaining person with the lightest remaining person if their combined weight allows it; otherwise, the heaviest person must take a boat alone.

## ⚙️ Algorithm

**Two pointers + greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`two-pointers` `greedy` `sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r=0,len(people)-1
        boats=0
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
            r-=1
            boats+=1
        return boats
```

</details>
