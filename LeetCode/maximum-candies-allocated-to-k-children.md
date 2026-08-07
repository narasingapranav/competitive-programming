# 🟠 maximum-candies-allocated-to-k-children — Maximum Candies Allocated to K Children

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Find the maximum equal number of candies that can be allocated to each of k children, given that each child can receive candies from at most one pile.

## 🔍 Key Observation

The total number of children that can be served with x candies per child decreases monotonically as x increases, enabling binary search on the answer.

## ⚙️ Algorithm

**Binary search on answer**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log(max(candies)))` | `O(n)` |

## 🏷️ Tags

`binary-search` `greedy` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l=1
        h=max(candies)
        while l<=h:
            mid=l+(h-l)//2
            ans=sum([i//mid for i in candies])
            if ans>=k:
                l=mid+1
            else:
                h=mid-1
        return h
```

</details>
