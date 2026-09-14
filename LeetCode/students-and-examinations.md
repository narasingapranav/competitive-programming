# 🟠 students-and-examinations — Students and Examinations

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/students-and-examinations/) &nbsp;|&nbsp; **Solved:** 2026-05-20

---

## 📝 Summary

Accepted solution for Students and Examinations on LeetCode.

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
select s.student_id , s.student_name , su.subject_name,count(e.student_id) as attended_exams from Students s cross join Subjects su left join Examinations e on s.student_id =e.student_id and su.subject_name=e.subject_name group by s.student_id , s.student_name ,su.subject_name order by s.student_id ,su.subject_name
```

</details>
