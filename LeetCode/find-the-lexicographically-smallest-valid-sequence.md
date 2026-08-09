# 🟠 find-the-lexicographically-smallest-valid-sequence — Find the Lexicographically Smallest Valid Sequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Find the lexicographically smallest sequence of indices in word1 that can form word2 with at most one character mismatch.

## 🔍 Key Observation

Precomputing the latest valid matching positions for every suffix of word2 allows us to greedily pick the smallest index for each character of word2, utilizing our single allowed mismatch at the earliest possible opportunity.

## ⚙️ Algorithm

**Greedy with Suffix Match Precomputation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n + m)` | `O(m)` |

## 🏷️ Tags

`greedy` `two pointers` `string` `suffix array`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int[] validSequence(String word1, String word2) {
        int n=word1.length();
        int m=word2.length();
        int[] last = new int[m];
        Arrays.fill(last,-1);
        int i=n-1;
        int j=m-1;
        while(i>=0 && j>=0){
            if (word1.charAt(i)==word2.charAt(j)){
                last[j--]=i;
            }
            i--;
        }
        int[] ans=new int[m];
        boolean canchange=true;
        i=0;
        j=0;
        while (i<n && j<m){
            if (word1.charAt(i)==word2.charAt(j)){
                ans[j++]=i;
            }
            else if(canchange && (j==m-1 || i<last[j+1])){
                ans[j++]=i;
                canchange=false;
            }
            if (j==m){
                return ans;
            }
            i++;
        }
        return new int[0];
    }
}
```

</details>
