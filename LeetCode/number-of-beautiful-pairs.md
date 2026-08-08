# 🟠 number-of-beautiful-pairs — Number of Beautiful Pairs

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-beautiful-pairs/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Count the number of index pairs (i, j) with i < j such that the first digit of nums[i] and the last digit of nums[j] are coprime.

## 🔍 Key Observation

The problem only depends on the first digit of the left element and the last digit of the right element having a greatest common divisor equal to 1.

## ⚙️ Algorithm

**Brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n)` |

## 🏷️ Tags

`math` `array` `number-theory` `brute-force`

<details>
<summary>💻 View solution</summary>

```python
from math import gcd
class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        n = len(nums)
        firstDig = [int(str(x)[0]) for x in nums]
        lastDig = [x % 10 for x in nums]
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                if gcd(firstDig[i], lastDig[j]) == 1:
                    cnt += 1
        return cnt
```

</details>
