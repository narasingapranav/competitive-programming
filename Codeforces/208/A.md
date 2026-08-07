# 🔵 208A — Dubstep

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/208/A) &nbsp;|&nbsp; **Solved:** 2026-08-02

---

## 📝 Summary

Restore the original song title from a remixed string by removing all inserted occurrences of the word 'WUB' and joining the original words with spaces.

## 🔍 Key Observation

The inserted word 'WUB' acts as a delimiter separating the original words, so splitting by 'WUB' and filtering out empty strings reconstructs the original song.

## ⚙️ Algorithm

**String splitting and filtering**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`strings` `implementation`

<details>
<summary>💻 View solution</summary>

```python
s=input()
s=s.split("WUB")
s=[i for i in s if i!=""]
print(" ".join(s))
```

</details>
