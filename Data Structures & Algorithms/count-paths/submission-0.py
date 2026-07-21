class Solution:
    def unique(self, i: int, j: int, m: int, n: int, dp: List[List]) -> int:
        if i == m or j == n:
            return 0
        if i == m-1 or j == n-1:
            return 1

        if dp[i][j] is not None:
            return dp[i][j]
        
        down = self.unique(i+1, j, m, n, dp)
        right = self.unique(i, j+1, m, n, dp)
        dp[i][j] = down + right

        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n+1)] for _ in range(m+1)]
        return self.unique(0,0,m,n,dp)
        