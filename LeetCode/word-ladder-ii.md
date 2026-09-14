# 🟠 word-ladder-ii — Word Ladder II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/word-ladder-ii/) &nbsp;|&nbsp; **Solved:** 2026-02-28

---

## 📝 Summary

Accepted solution for Word Ladder II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS) + Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^5) (estimated -- 5 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`graph` `hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset=set(wordList)
        if endWord not in wordset:
            return []
        parents=defaultdict(list)
        visited=set()
        found=False
        level={beginWord}
        while level and not found:
            nextlevel=set()
            for i in level:
                visited.add(i)
            for w in level :
                for i in range(len(w)):
                    for ch in 'qwertyuiopasdfghjklzxcvbnm':
                        if ch== w[i]:
                            continue
                        newword=w[:i]+ch+w[i+1 :]
                        if newword in wordset and newword not in visited:
                            if newword == endWord:
                                found =True
                            nextlevel.add(newword)
                            parents[newword].append(w)
            level=nextlevel
        path=[endWord]
        res=[]
        def back(endWord):
            if endWord==beginWord:
                res.append(path[::-1])
                return
            for parent in parents[endWord]:
                path.append(parent)
                back(parent)
                path.pop()
        if found:
            back(endWord)
        return res
```

</details>
