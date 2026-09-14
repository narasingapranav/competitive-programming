# 🟠 number-of-even-and-odd-bits — Number of Even and Odd Bits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-even-and-odd-bits/) &nbsp;|&nbsp; **Solved:** 2025-12-08

---

## 📝 Summary

Accepted solution for Number of Even and Odd Bits on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int[] evenOddBit(int n) {
        int e=0,o=0;
        int pos=0;
        while (n>0){
            if ((n&1)==1){
                if (pos%2==0) e++;
                else o++;   
            }
            n>>=1;
            pos++;
        }
        return new int[]{e,o};
    }
}
```

</details>
