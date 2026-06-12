class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [False] * n
        start = 0
        max_len = 1
        for i in range(n-1, -1, -1):
            dp[i] = True
            for j in range(n-1, i, -1):
                dp[j] = (
                    s[i] == s[j] and (j-i < 3 or dp[j-1])
                )
            
                if dp[j] and j-i+1 > max_len:
                    start = i
                    max_len = j-i+1
        return s[start:start + max_len]

        