# 🟠 the-number-of-employees-which-report-to-each-employee — The Number of Employees Which Report to Each Employee

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/) &nbsp;|&nbsp; **Solved:** 2026-05-23

---

## 📝 Summary

Accepted solution for The Number of Employees Which Report to Each Employee on LeetCode.

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
select e1.employee_id ,e1.name,count(*) as reports_count , round(avg(e2.age)) as average_age from Employees e1 join Employees e2 on e1.employee_id =e2.reports_to group by employee_id order by employee_id
```

</details>
