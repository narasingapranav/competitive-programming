# 🟠 group-anagrams — Group Anagrams

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/group-anagrams/) &nbsp;|&nbsp; **Solved:** 2026-08-10

---

## 📝 Summary

Group an array of strings into sublists where each sublist contains words that are anagrams of one another.

## 🔍 Key Observation

Sorting the characters of a string produces a canonical representation that is identical for all anagrams, allowing them to be grouped using a hash map key.

## ⚙️ Algorithm

**Hash map with character sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N * K log K)` | `O(N * K)` |

## 🏷️ Tags

`hash-table` `string` `sorting`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,ArrayList<String>> d =new HashMap<>();
        List<List<String>> res= new ArrayList<>();
        for(String i:strs){
            char[] arr=i.toCharArray();
            Arrays.sort(arr);
            String b=new String(arr);
            if(!d.containsKey(b)){
                d.put(b,new ArrayList<>());
            }
            d.get(b).add(i);
        }
        res.addAll(d.values());
        return res;
    }
}
```

</details>
