# 🟠 sum-of-subarray-minimums — Sum of Subarray Minimums

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sum-of-subarray-minimums/) &nbsp;|&nbsp; **Solved:** 2026-08-13

---

## 📝 Summary

Calculate the sum of the minimum elements across all possible contiguous subarrays of a given array, modulo 10^9 + 7.

## 🔍 Key Observation

Instead of generating all subarrays, determine the number of subarrays where each element is the minimum by finding the index of its previous strictly smaller element and next smaller-or-equal element using a monotonic stack.

## ⚙️ Algorithm

**Monotonic stack**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`monotonic-stack` `array` `stack` `combinatorics`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD=10**9 +7
        res=0
        st=[]
        for i in range(len(arr)+1):
            while st and (i==len(arr) or arr[st[-1]]>=arr[i]):
                x=st.pop()
                lb=-1 if len(st)==0 else st[-1]
                ub=i
                c=((x-lb)*(ub-x))%MOD
                res=(res+arr[x]*c)%MOD
            st.append(i)
        return res
```

</details>
