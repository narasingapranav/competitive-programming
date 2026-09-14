class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cnt = defaultdict(int)
        left = 0
        for i, ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans