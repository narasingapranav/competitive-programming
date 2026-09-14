# 🟠 average-time-of-process-per-machine — Average Time of Process per Machine

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/average-time-of-process-per-machine/) &nbsp;|&nbsp; **Solved:** 2026-05-20

---

## 📝 Summary

Accepted solution for Average Time of Process per Machine on LeetCode.

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
select a1.machine_id , round(avg(a2.timestamp-a1.timestamp),3) as processing_time from Activity a1 join Activity a2 on a1.machine_id = a2.machine_id and a1.process_id=a2.process_id and a1.activity_type='start' and a2.activity_type='end' group by a1.machine_id
```

</details>
