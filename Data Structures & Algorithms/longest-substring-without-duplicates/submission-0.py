class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(hashmap[s[right]] + 1, left)
            hashmap[s[right]] = right
            res = max(res, (right - left) + 1)
        return res