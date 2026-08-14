# 🔵 1788A — One and Two

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1788/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Find the smallest index k such that the product of the first k elements equals the product of the remaining elements in an array containing only 1s and 2s.

## 🔍 Key Observation

Since the array contains only 1s and 2s, two subsegment products are equal if and only if they contain the same number of 2s; thus, a valid index exists if and only if the total count of 2s is even.

## ⚙️ Algorithm

**Prefix counting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`math` `greedy` `implementation`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=a.count(2)
    if c&1:
        print(-1)
    else:
        n=c//2
        b=0
        ans=0
        for i in range(len(a)):
            if a[i]==2:
                b+=1
            if b==n:
                ans=i+1
                break
        print(ans)
```

</details>
