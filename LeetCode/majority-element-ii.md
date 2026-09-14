# 🟠 majority-element-ii — Majority Element II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/majority-element-ii/) &nbsp;|&nbsp; **Solved:** 2026-03-03

---

## 📝 Summary

Accepted solution for Majority Element II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        cnt1,cnt2=0,0
        ele1,ele2=float('-inf'),float('-inf')
        for i in nums:
            if cnt1==0 and ele2!=i:
                cnt1=1
                ele1=i
            elif cnt2==0 and ele1!=i:
                cnt2=1
                ele2=i
            elif i==ele1:
                cnt1+=1
            elif i==ele2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1=cnt2=0
        for i in nums:
            if i==ele1:
                cnt1+=1
            elif i==ele2:
                cnt2+=1
        res=[]
        if cnt1>n//3:
            res.append(ele1)
        if cnt2>n//3:
            res.append(ele2)
        return res
```

</details>
