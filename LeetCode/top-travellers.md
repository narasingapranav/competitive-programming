# 🟠 top-travellers — Top Travellers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/top-travellers/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Accepted solution for Top Travellers on LeetCode.

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
select u.name, coalesce(sum(d.distance),0) as travelled_distance from Users u left join Rides d on u.id=d.user_id group by u.id,u.name order by travelled_distance desc ,u.name
```

</details>
