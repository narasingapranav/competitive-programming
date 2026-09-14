# 🟠 managers-with-at-least-5-direct-reports — Managers with at Least 5 Direct Reports

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/) &nbsp;|&nbsp; **Solved:** 2026-05-20

---

## 📝 Summary

Accepted solution for Managers with at Least 5 Direct Reports on LeetCode.

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
select name from Employee where id in (select managerId from Employee group by managerId having count(*)>=5)
```

</details>
