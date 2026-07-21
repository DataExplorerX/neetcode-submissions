class Solution:
    def lcs(self, i: int, j: int, text1: str, text2: str, dp: List[List]) -> int:
        m, n = len(text1), len(text2)
        if i >= m or j >= n:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]
        
        if text1[i] == text2[j]:
            dp[i][j] = 1 + self.lcs(i+1, j+1, text1, text2, dp)
        else:
            dp[i][j] = max(self.lcs(i+1, j, text1, text2, dp), self.lcs(i, j+1, text1, text2, dp))
        
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[None for _ in range(n+1)] for _ in range(m+1)]
        return self.lcs(0, 0,text1, text2, dp)
        