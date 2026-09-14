# 🟠 friend-requests-ii-who-has-the-most-friends — Friend Requests II: Who Has the Most Friends

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/) &nbsp;|&nbsp; **Solved:** 2026-05-25

---

## 📝 Summary

Accepted solution for Friend Requests II: Who Has the Most Friends on LeetCode.

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
WITH all_ids AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)

SELECT id, COUNT(id) AS num
FROM all_ids
GROUP BY id
ORDER BY num DESC
LIMIT 1;
```

</details>
