# 🟠 prime-number-of-set-bits-in-binary-representation — Prime Number of Set Bits in Binary Representation

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) &nbsp;|&nbsp; **Solved:** 2026-02-21

---

## 📝 Summary

Accepted solution for Prime Number of Set Bits in Binary Representation on LeetCode.

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
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isprime(num):
            count=0
            for i in range(1,num+1):
                if num%i==0:
                    count+=1
            if count==2:
                return True
            return False
        c=0
        for i in range (left,right+1):
            b=bin(i)[2:]
            co=b.count('1')
            if isprime(co):
                c+=1
        return c
```

</details>
