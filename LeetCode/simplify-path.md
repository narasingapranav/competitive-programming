# 🟠 simplify-path — Simplify Path

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/simplify-path/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Given an absolute Unix-style path, simplify it to its canonical path by resolving relative directory references such as '.' and '..'.

## 🔍 Key Observation

Splitting the path by slashes isolates directory components, allowing a stack to easily simulate directory navigation by pushing valid directory names and popping when encountering '..'.

## ⚙️ Algorithm

**Stack**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(N)` |

## 🏷️ Tags

`stack` `string` `simulation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        p=[i for i in path.split('/') if i!=""]
        st=[]
        for i in p:
            if i=='.':
                continue
            if i!='..':
                st.append(i)
            else:
                if st:
                    st.pop()
                else:
                    continue
        return '/'+'/'.join(st)
```

</details>
