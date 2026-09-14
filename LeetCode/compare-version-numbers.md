# 🟠 compare-version-numbers — Compare Version Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/compare-version-numbers/) &nbsp;|&nbsp; **Solved:** 2025-12-23

---

## 📝 Summary

Accepted solution for Compare Version Numbers on LeetCode.

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
    def compareVersion(self, v1: str, v2: str) -> int:
        v1,v2=list(map(int,v1.split('.'))),list(map(int,v2.split('.')))
        for rev1,rev2 in zip_longest(v1,v2,fillvalue=0):
            if rev1==rev2:
                continue
            return -1 if rev1<rev2 else 1
        return 0
```

</details>
