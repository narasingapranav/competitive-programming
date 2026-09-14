# 🟠 two-sum — Two Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/two-sum/) &nbsp;|&nbsp; **Solved:** 2026-02-27

---

## 📝 Summary

Accepted solution for Two Sum on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n log n) (estimated -- sort detected)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def twoSum(self,arr,k):
        l=[(arr[i],i) for i in range(len(arr))]
        l.sort()
        i=0
        j=len(arr)-1
        while i<j:
            if l[i][0]+l[j][0] > k:
                j-=1
            elif l[i][0]+l[j][0] < k:
                i+=1
            else:
                return [l[i][1],l[j][1]]
        return [-1,-1]
```

</details>
