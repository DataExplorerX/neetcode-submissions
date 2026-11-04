class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i, j = 0, 0
        max_len = 0
        while j < n:
            if s[j] not in s[i:j]:
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                i += 1
        return max_len
        