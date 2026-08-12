# 🟠 length-of-longest-subarray-with-at-most-k-frequency — Length of Longest Subarray With at Most K Frequency

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/) &nbsp;|&nbsp; **Solved:** 2026-08-12

---

## 📝 Summary

Find the maximum length of a contiguous subarray in which no element appears more than k times.

## 🔍 Key Observation

A sliding window can track element frequencies, expanding with a right pointer and shrinking from the left whenever adding an element causes its frequency to exceed k.

## ⚙️ Algorithm

**Sliding window**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`sliding-window` `hash-table` `two-pointers` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n, cnt=len(nums), 0
        freq=defaultdict(int)
        l=0
        for r, x in enumerate(nums):
            freq[x]+=1
            while freq[x]>k:
                freq[nums[l]]-=1
                l+=1
            cnt=max(cnt, r-l+1)
        return cnt
```

</details>
