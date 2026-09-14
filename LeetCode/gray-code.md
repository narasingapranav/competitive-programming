# 🟠 gray-code — Gray Code

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/gray-code/) &nbsp;|&nbsp; **Solved:** 2025-12-08

---

## 📝 Summary

Accepted solution for Gray Code on LeetCode.

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
    public List<Integer> grayCode(int n) {
        List<Integer> l = new ArrayList<>();
        int s=1<<n;
        for (int i=0;i<s;i++){
            int g=i ^ (i>>1);
            l.add(g);
        }
        return l;
    }
}
```

</details>
