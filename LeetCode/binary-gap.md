# 🟠 binary-gap — Binary Gap

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-gap/) &nbsp;|&nbsp; **Solved:** 2026-02-22

---

## 📝 Summary

Accepted solution for Binary Gap on LeetCode.

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

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        md=0
        cd=0
        flag=False
        while n>0:
            a=n%2
            if a==1:
                if flag:
                    md=max(md,cd)
                cd=1
                flag=True
            else:
                if flag:
                    cd+=1
            n//=2
        return md
```

</details>
