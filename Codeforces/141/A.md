# 🔵 141A — Amusing Joke

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/141/A) &nbsp;|&nbsp; **Solved:** 2026-08-03

---

## 📝 Summary

Determine if the letters from a pile can be rearranged to exactly form both the guest's and host's names combined.

## 🔍 Key Observation

The original letter order does not matter; the combined frequency of each character in the first two strings must equal its frequency in the third string.

## ⚙️ Algorithm

**Frequency counting / Hash map comparison**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(1)` |

## 🏷️ Tags

`strings` `implementation` `hash map`

<details>
<summary>💻 View solution</summary>

```python
s=input()
l=input()
p=input()
d={}
for i in s:
    d[i]=d.get(i,0)+1
for i in l:
    d[i]=d.get(i,0)+1
f={}
for i in p:
    f[i]=f.get(i,0)+1
if d==f:
    print("YES")
else:
    print("NO")
    
```

</details>
