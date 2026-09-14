# 🟠 smallest-missing-multiple-of-k — Smallest Missing Multiple of K

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-missing-multiple-of-k/) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

Accepted solution for Smallest Missing Multiple of K on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int missingMultiple(int[] nums, int k) {
        HashSet<Integer> s= new HashSet<>();
        for (int i:nums){
            s.add(i);
        }
        int m=Arrays.stream(nums).max().getAsInt();;
        for(int i=k;i<=m+k;i+=k){
            if (!s.contains(i)){
                return i;
            }
        }
        return 0;
    }
}
```

</details>
