# 🟠 user-activity-for-the-past-30-days-i — User Activity for the Past 30 Days I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) &nbsp;|&nbsp; **Solved:** 2026-05-22

---

## 📝 Summary

Accepted solution for User Activity for the Past 30 Days I on LeetCode.

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
select activity_date as day , count(distinct user_id) as active_users from Activity where (activity_date > "2019-06-27" and activity_date <= "2019-07-27" ) group by activity_date
```

</details>
