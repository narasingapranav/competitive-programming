# 🔵 158B — Taxi

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/158/B) &nbsp;|&nbsp; **Solved:** 2026-08-04

---

## 📝 Summary

Determine the minimum number of taxis needed to transport groups of schoolchildren of sizes 1 to 4, given that each taxi can carry at most 4 people and a single group cannot be split across taxis.

## 🔍 Key Observation

Greedily match groups to fill taxis efficiently: groups of size 4 take their own taxi, size 3 pairs with size 1, size 2 pairs with size 2 (or leftover size 1s), and remaining size 1s are grouped by fours.

## ⚙️ Algorithm

**Greedy algorithm**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`greedy` `implementation`

<details>
<summary>💻 View solution</summary>

```python
n = int(input())
cnt = [0] * 5
for x in map(int, input().split()):
    cnt[x] += 1
ans = cnt[4]
ans += cnt[3]
cnt[1] = max(0, cnt[1] - cnt[3])
ans += cnt[2] // 2
cnt[2] %= 2
if cnt[2]:
    ans += 1
    cnt[1] = max(0, cnt[1] - 2)
ans += (cnt[1] + 3) // 4
print(ans)
```

</details>
