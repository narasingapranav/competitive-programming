# 🟠 primary-department-for-each-employee — Primary Department for Each Employee

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/primary-department-for-each-employee/) &nbsp;|&nbsp; **Solved:** 2026-05-23

---

## 📝 Summary

Accepted solution for Primary Department for Each Employee on LeetCode.

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
select employee_id , department_id from Employee where primary_flag='Y' union select employee_id , department_id from Employee group by employee_id having count(*)=1
```

</details>
