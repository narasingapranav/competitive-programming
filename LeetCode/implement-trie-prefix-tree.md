# 🟠 implement-trie-prefix-tree — Implement Trie (Prefix Tree)

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/) &nbsp;|&nbsp; **Solved:** 2026-08-06

---

## 📝 Summary

Implement a Trie (prefix tree) data structure that supports inserting words, searching for exact words, and checking if any previously inserted word starts with a given prefix.

## 🔍 Key Observation

A Trie structures words as paths in a tree where each node represents a character transition, enabling fast lookup of shared prefixes without re-scanning characters.

## ⚙️ Algorithm

**Trie (Prefix Tree)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m) per operation, where m is the length of the string/prefix` | `O(N * m) overall, where N is the total number of words inserted and m is the average word length` |

## 🏷️ Tags

`trie` `design` `string` `hash-table`

<details>
<summary>💻 View solution</summary>

```python
class Trie:

    def __init__(self):
        self.child={}
        self.eow=False

    def insert(self, word: str) -> None:
        node=self
        for i in word:
            if i not in node.child:
                node.child[i]=Trie()
            node=node.child[i]
        node.eow=True

    def search(self, word: str) -> bool:
        node=self
        for i in word:
            if i not in node.child:
                return False
            node=node.child[i]
        return node.eow

    def startsWith(self, prefix: str) -> bool:
        node=self
        for i in prefix:
            if i not in node.child:
                return False
            node=node.child[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

</details>
