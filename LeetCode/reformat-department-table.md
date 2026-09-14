# 🟠 reformat-department-table — Reformat Department Table

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reformat-department-table/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Accepted solution for Reformat Department Table on LeetCode.

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

SELECT id,
    MAX(CASE WHEN month ='Jan' THEN revenue END) AS Jan_Revenue,
    MAX(CASE WHEN month ='Feb' THEN revenue END) AS Feb_Revenue,
    MAX(CASE WHEN month ='Mar' THEN revenue END) AS Mar_Revenue,
    MAX(CASE WHEN month ='Apr' THEN revenue END) AS Apr_Revenue,
    MAX(CASE WHEN month ='May' THEN revenue END) AS May_Revenue,
    MAX(CASE WHEN month ='Jun' THEN revenue END) AS Jun_Revenue,
    MAX(CASE WHEN month ='Jul' THEN revenue END) AS Jul_Revenue,
    MAX(CASE WHEN month ='Aug' THEN revenue END) AS Aug_Revenue,
    MAX(CASE WHEN month ='Sep' THEN revenue END) AS Sep_Revenue,
    MAX(CASE WHEN month ='Oct' THEN revenue END) AS Oct_Revenue,
    MAX(CASE WHEN month ='Nov' THEN revenue END) AS Nov_Revenue,
    MAX(CASE WHEN month ='Dec' THEN revenue END) AS Dec_Revenue
FROM DEPARTMENT
GROUP BY id
```

</details>
