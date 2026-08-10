# 🟠 decode-string — Decode String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/decode-string/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Given an encoded string with nested bracket patterns of the form `k[encoded_string]`, return the fully decoded string where `encoded_string` is repeated `k` times.

## 🔍 Key Observation

A stack naturally handles nested brackets by maintaining intermediate strings and multiplier counts, allowing inner expressions to be decoded and appended to outer contexts in LIFO order.

## ⚙️ Algorithm

**Stack-based parsing**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(N)` |

## 🏷️ Tags

`stack` `string` `parsing`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def decodeString(self, s: str) -> str:
        num=[]
        st=[]
        i=0
        res=""
        n=len(s)
        while i<n:
            if s[i].isdigit():
                x=0
                while i<n and s[i].isdigit():
                    x=x*10+int(s[i])
                    i+=1
                num.append(x)
                continue
            elif s[i]=='[':
                st.append("")
            elif s[i].isalpha():
                if st:
                    st[-1]+=s[i]
                else:
                    res+=s[i]
            else:
                popped=st.pop()
                popnum=num.pop()
                if st:
                    st[-1]+=popped*popnum
                else:
                    res+=popped*popnum
            i+=1
        return res
```

</details>
