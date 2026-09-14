# 🟠 department-highest-salary — Department Highest Salary

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/department-highest-salary/) &nbsp;|&nbsp; **Solved:** 2026-06-03

---

## 📝 Summary

Accepted solution for Department Highest Salary on LeetCode.

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
select d.name as Department , e.name as Employee, e.salary as Salary  from Employee e , Department d where e.departmentId=d.id and (e.departmentId,salary) in (select departmentId , max(salary) from Employee group by departmentId)
```

</details>
