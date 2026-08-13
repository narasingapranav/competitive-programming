# 🔵 1594C — Make Them Equal

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1594/C) &nbsp;|&nbsp; **Solved:** 2026-08-13

---

## 📝 Summary

Find the minimum number of operations needed to make all characters in a string equal to $c$, where picking a 1-based index $x$ replaces every character at index $i$ not divisible by $x$ with $c$.

## 🔍 Key Observation

At most two operations are ever required: 0 if the string is already all $c$, 1 if there exists an index $x$ whose multiples are all $c$, and 2 using indices $n-1$ and $n$ otherwise.

## ⚙️ Algorithm

**Greedy / Math**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`greedy` `math` `strings` `brute force`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n,c=input().split()
    n=int(n)
    s=input()
    allcount=[]
    for x in range(1,n+1):
        count=0
        for i in range(x,n+1,x):
            if s[i-1]!=c:
                count+=1
        allcount.append(count)
    if all(s[i] == c for i in range(n)):
        print(0)

    elif 0 in allcount:
        x = allcount.index(0) + 1
        print(1)
        print(x)

    else:
        print(2)
        print(n - 1, n)
```

</details>
