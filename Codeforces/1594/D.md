# 🔵 1594D — The Number of Imposters

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1594/D) &nbsp;|&nbsp; **Solved:** 2026-08-13

---

## 📝 Summary

Find the maximum possible number of imposters given a set of statements where players identify others as crewmates or imposters, or return -1 if the statements contain a contradiction.

## 🔍 Key Observation

Each statement defines a constraint between two players (same role for 'crewmate', opposite roles for 'imposter'). This forms connected components where fixing the role of one node determines the roles of all other nodes in that component; we greedily choose the role assignment that yields the maximum number of imposters per component.

## ⚙️ Algorithm

**DFS / Graph 2-Coloring**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n + m)` | `O(n + m)` |

## 🏷️ Tags

`graphs` `dfs` `bipartite` `dsu` `constructive algorithms`

<details>
<summary>💻 View solution</summary>

```python
from collections import defaultdict
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    graph=defaultdict(list)
    for _ in range(m):
        u,v,c=map(str,input().split())
        u,v=int(u)-1,int(v)-1
        w=1 if c=='imposter' else 0
        graph[u].append((v,w))
        graph[v].append((u,w))
    role=[-1]*n
    ans=0
    possible=True
    for i in range(n):
        if role[i]!=-1:
            continue
        st=[i]
        role[i]=0
        count=[1,0]
        while st:
            u=st.pop()
            for v,w in graph[u]:
                exp=role[u]^w
                if role[v]==-1:
                    role[v]=exp
                    count[exp]+=1
                    st.append(v)
                elif role[v]!=exp:
                    possible=False
                    break
            if not possible:
                break
        if not possible:
            break
        ans+=max(count)
    if not possible:
        print(-1)
    else:
        print(ans)
```

</details>
