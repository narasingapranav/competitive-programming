# 🟠 wiggle-subsequence — Wiggle Subsequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/wiggle-subsequence/) &nbsp;|&nbsp; **Solved:** 2026-08-06

---

## 📝 Summary

Find the length of the longest subsequence in an array such that the differences between consecutive elements strictly alternate between positive and negative.

## 🔍 Key Observation

We only need to extend the sequence when the direction of change alternates; greedily picking extreme local peaks and valleys maximizes the potential length.

## ⚙️ Algorithm

**Greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`greedy` `dynamic-programming` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        s1=1
        s2=1
        s1prev=nums[0]
        s2prev=nums[0]
        t1=1
        t2=-1
        for i in range(1,len(nums)):
            if nums[i]>s1prev:
                if t1==1:
                    s1prev=nums[i]
                    s1+=1
                    t1=-1
                else:
                    s1prev=max(s1prev,nums[i])
            elif nums[i]<s1prev:
                if t1==-1:
                    s1prev=nums[i]
                    s1+=1
                    t1=1
                else:
                    s1prev=min(s1prev,nums[i])
            if nums[i]>s2prev:
                if t2==1:
                    s2prev=nums[i]
                    s2+=1
                    t2=-1
                else:
                    s2prev=max(s2prev,nums[i])
            elif nums[i]<s2prev:
                if t2==-1:
                    s2prev=nums[i]
                    s2+=1
                    t2=1
                else:
                    s2prev=min(s2prev,nums[i])
        return max(s1,s2)
```

</details>
