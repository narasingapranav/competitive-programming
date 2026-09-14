# 🟠 employees-earning-more-than-their-managers — Employees Earning More Than Their Managers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/employees-earning-more-than-their-managers/) &nbsp;|&nbsp; **Solved:** 2025-11-20

---

## 📝 Summary

Accepted solution for Employees Earning More Than Their Managers on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    a=employee.merge(employee,left_on="managerId",right_on="id",suffixes=("","boss"))
    r=a[a["salary"]>a["salaryboss"]]
    return r[["name"]].rename(columns={"name":"Employee"})
```

</details>
