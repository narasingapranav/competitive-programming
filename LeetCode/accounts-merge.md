# 🟠 accounts-merge — Accounts Merge

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/accounts-merge/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Given a list of accounts containing a name and several emails, merge accounts that share common emails and return each merged account with sorted emails.

## 🔍 Key Observation

Accounts sharing at least one email address belong to the same person, forming connected components among emails that can be efficiently tracked using Union-Find.

## ⚙️ Algorithm

**Union-Find (Disjoint Set Union)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N log N)` | `O(N)` |

## 🏷️ Tags

`disjoint-set-union` `graph` `hash-table` `sorting`

<details>
<summary>💻 View solution</summary>

```python
class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
    def find(self,x):
        if x==self.parent[x]:
            return x
        return self.find(self.parent[x])
    def union(self,x,y):
        pa=self.find(x)
        pb=self.find(y)
        if pa!=pb:
            self.parent[pb]=pa
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        id={}
        en={}
        idx=0
        for i in accounts:
            name=i[0]
            for j in i[1:]:
                if j not in id:
                    id[j]=idx
                    idx+=1
                en[j]=name
        uf=UnionFind(idx)
        for i in accounts:
            first=id[i[1]]
            for j in i[2:]:
                uf.union(first,id[j])
        groups={}
        for email in id:
            root=uf.find(id[email])
            if root not in groups:
                groups[root]=[]
            groups[root].append(email)
        ans=[]
        for r,e in groups.items():
            e.sort()
            name=en[e[0]]
            ans.append([name]+e)
        return ans
```

</details>
