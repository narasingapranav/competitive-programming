# 🟠 substring-with-concatenation-of-all-words — Substring with Concatenation of All Words

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) &nbsp;|&nbsp; **Solved:** 2026-08-11

---

## 📝 Summary

Find all starting indices in string `s` where a substring is a concatenation of all words in `words` in any order, given that all words have the exact same length.

## 🔍 Key Observation

Since every word has equal length `L`, we can split the sliding window search into `L` offset passes and process fixed-length word chunks independently using word frequencies.

## ⚙️ Algorithm

**Sliding Window + Hash Map**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N * L)` | `O(M * L)` |

## 🏷️ Tags

`sliding-window` `hash-table` `string` `two-pointers`

<details>
<summary>💻 View solution</summary>

```java
class Solution{
    public List<Integer> findSubstring(String s, String[] words){
        HashMap<String,Integer> hm= new HashMap<>();
        List<Integer> res= new ArrayList<>();
        for(String s1:words){
            hm.put(s1,hm.getOrDefault(s1,0)+1);
        }
        int len = words[0].length();
        int n = words.length;
        for (int offset = 0; offset < len; offset++) {
            int left = offset;
            int c = 0;
            HashMap<String,Integer> window = new HashMap<>();
            for (int j=offset; j+len<=s.length(); j+=len) {
                String x=s.substring(j,j+len);
                if(!hm.containsKey(x)){
                    window.clear();
                    c=0;
                    left=j+len;
                    continue;
                }
                c++;
                window.put(x,window.getOrDefault(x,0)+1);
                while(window.get(x)>hm.get(x)){
                    String y=s.substring(left,left+len);
                    int count=window.get(y);
                    window.put(y,count-1);
                    c--;
                    left+=len;
                }
                if(c==n){
                    res.add(left);
                    String y=s.substring(left,left+len);
                    int count=window.get(y);
                    window.put(y,count-1);
                    c--;
                    left+=len;
                }
            }
        }
        return res;
    }
}
```

</details>
