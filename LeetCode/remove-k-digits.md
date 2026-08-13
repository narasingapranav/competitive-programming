# 🟠 remove-k-digits — Remove K Digits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-k-digits/) &nbsp;|&nbsp; **Solved:** 2026-08-13

---

## 📝 Summary

Given a string representing a non-negative integer num and an integer k, remove k digits from the string to form the smallest possible number.

## 🔍 Key Observation

To minimize the value of a number, smaller digits should appear at higher place values (leftmost); thus, we greedily pop larger preceding digits whenever a smaller digit is encountered.

## ⚙️ Algorithm

**Monotonic stack + greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`monotonic-stack` `greedy` `string`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in num:
            while st and k>0 and st[-1]>i:
                st.pop()
                k-=1
            st.append(i)
        while k>0:
            st.pop()
            k-=1
        res= "".join(st).lstrip('0')
        return res if res!="" else '0'
```

</details>
