# 🟠 tuple-with-same-product — Tuple with Same Product

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/tuple-with-same-product/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Find the number of tuples (a, b, c, d) of distinct elements from an array such that a * b = c * d.

## 🔍 Key Observation

For every pair of distinct pairs (a, b) and (c, d) that yield the same product, there are 8 valid tuple permutations of (a, b, c, d).

## ⚙️ Algorithm

**Hash map frequency counting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n^2)` |

## 🏷️ Tags

`hash-table` `combinatorics` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p=nums[i]*nums[j]
                d[p]=d.get(p,0)+1
        ans=0
        for c in d.values():
            ans+=8*c*(c-1)//2
        return ans
```

</details>
