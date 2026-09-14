# 🟠 word-frequency — Word Frequency

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/word-frequency/) &nbsp;|&nbsp; **Solved:** 2026-02-22

---

## 📝 Summary

Accepted solution for Word Frequency on LeetCode.

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
# Read from the file words.txt and output the word frequency list to stdout.
tr -s ' ' '\n' < words.txt | \
sort | \
uniq -c | \
sort -nr | \
awk '{print $2, $1}'
```

</details>
