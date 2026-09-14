# 🟠 employees-whose-manager-left-the-company — Employees Whose Manager Left the Company

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/employees-whose-manager-left-the-company/) &nbsp;|&nbsp; **Solved:** 2026-05-22

---

## 📝 Summary

Accepted solution for Employees Whose Manager Left the Company on LeetCode.

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
# Write your MySQL query statement below
select employee_id from Employees where salary<30000 and manager_id not in(select employee_id from Employees) order by employee_id asc
```

</details>
