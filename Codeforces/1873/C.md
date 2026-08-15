# 🔵 1873C — Target Practice

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1873/C) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Calculate the total score of shots marked as 'X' on a 10x10 target board, where points increase from 1 to 5 as shots get closer to the center ring.

## 🔍 Key Observation

The point value of a shot at row i and column j depends on how close it is to the boundary, determined by the distance of the cell from the nearest edge of the 10x10 grid.

## ⚙️ Algorithm

**Grid Traversal**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `matrices` `math`

<details>
<summary>💻 View solution</summary>

```python
t=int(input())
for _ in range(t):
    mat=[input() for _ in range(10)]
    score=0
    for i in range(10):
        for j in range(10):
            if mat[i][j]=="X":
                if i==0 or i==9 or j==0 or j==9:
                    score+=1
                elif i==1 or i==8 or j==1 or j==8:
                    score+=2
                elif i==2 or i==7 or j==2 or j==7:
                    score+=3
                elif i==3 or i==6 or j==3 or j==6:
                    score+=4
                elif i==4 or i==5 or j==4 or j==5:
                    score+=5
    print(score)
```

</details>
