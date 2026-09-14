# 🟠 transpose-file — Transpose File

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/transpose-file/) &nbsp;|&nbsp; **Solved:** 2026-02-22

---

## 📝 Summary

Accepted solution for Transpose File on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```
# Read from the file file.txt and print its transposed content to stdout.
awk '
{
    for (i = 1; i <= NF; i++) {
        if (NR == 1) {
            result[i] = $i
        } else {
            result[i] = result[i] " " $i
        }
    }
}
END {
    for (i = 1; i <= length(result); i++) {
        print result[i]
    }
}' file.txt
```

</details>
