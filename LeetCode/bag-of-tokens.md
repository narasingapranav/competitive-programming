# 🟠 bag-of-tokens — Bag of Tokens

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-java-007396?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/bag-of-tokens/) &nbsp;|&nbsp; **Solved:** 2026-08-11

---

## 📝 Summary

Given an initial power and an array of token values, maximize your score by playing tokens face up (spend power equal to token value to gain 1 score) or face down (spend 1 score to gain power equal to token value).

## 🔍 Key Observation

To maximize score, we should greedily buy the cheapest available tokens face up to gain score and sell the most expensive available tokens face down to gain power.

## ⚙️ Algorithm

**Two pointers + Greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(1)` |

## 🏷️ Tags

`greedy` `two-pointers` `sorting` `array`

<details>
<summary>💻 View solution</summary>

```java
class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int l=0;
        int h=tokens.length-1;
        int s=0;
        int m=0;
        while (l<=h){
            if(power>=tokens[l]){
                s++;
                power-=tokens[l];
                m=Math.max(m,s);
                l++;
            }
            else if(s>=1){
                s--;
                power+=tokens[h];
                h--;
            }
            else{
                break;
            }
        }
        return m;
    }
}
```

</details>
