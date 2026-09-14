# 🟠 asteroid-collision — Asteroid Collision

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/asteroid-collision/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Accepted solution for Asteroid Collision on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            while st and st[-1]>0 and i<0:
                if st[-1]<-i:
                    st.pop()
                    continue
                elif st[-1]==-i:
                    st.pop()
                break
            else:
                st.append(i)
        return st
```

</details>
