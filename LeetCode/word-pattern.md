# 🟠 word-pattern — Word Pattern

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/word-pattern/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Determine if a string of space-separated words follows a given character pattern, establishing a bijection between characters in the pattern and words in the string.

## 🔍 Key Observation

A valid pattern match requires a two-way (bijective) mapping, meaning each character must map to a unique word, and each word must uniquely map back to the same character.

## ⚙️ Algorithm

**Two HashMaps / Hash Table Mapping**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N + M)` | `O(N + M)` |

## 🏷️ Tags

`hash-table` `string`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words= s.split(" ");
        if(pattern.length()!=words.length){
            return false;
        }
        HashMap<Character,String> c2w=new HashMap<>();
        HashMap<String,Character> w2c=new HashMap<>();
        for(int i=0;i<words.length;i++){
            if (c2w.containsKey(pattern.charAt(i)) && !c2w.get(pattern.charAt(i)).equals(words[i])){
                return false;
            }
            if (w2c.containsKey(words[i]) &&! w2c.get(words[i]).equals(pattern.charAt(i))){
                return false;
            }
            c2w.put(pattern.charAt(i),words[i]);
            w2c.put(words[i],pattern.charAt(i));
        }
        return true;
    }
}
```

</details>
