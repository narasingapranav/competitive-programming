# 🔵 1901A — Line Trip

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1901/A) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Find the minimum fuel tank capacity required to travel from origin 0 to point x and back, given a list of gas station coordinates along the route.

## 🔍 Key Observation

The required tank capacity is determined by the maximum gap between adjacent refueling points, keeping in mind that the distance from the last station to x must be covered twice consecutively without refueling.

## ⚙️ Algorithm

**Greedy array traversal**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`greedy` `math` `implementation`

<details>
<summary>💻 View solution</summary>

```python
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = a[0]
    for i in range(1, n):
        ans = max(ans, a[i] - a[i - 1])
    ans = max(ans, 2 * (x - a[-1]))
    print(ans)
```

</details>
