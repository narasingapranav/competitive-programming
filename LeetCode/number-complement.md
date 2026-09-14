# 🟠 number-complement — Number Complement

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-complement/) &nbsp;|&nbsp; **Solved:** 2025-12-08

---

## 📝 Summary

Accepted solution for Number Complement on LeetCode.

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
    public int findComplement(int num) {
        int mask=0;
        int temp=num;
        while(temp >0){
            mask=(mask<<1) |1;
            temp>>=1;
        }
        return num^mask;
    }
}
```

</details>
