class Solution:
    def coinChange(self, i: int, amount: int, coins: List[int], dp: List[List[int]]) -> int:
        n = len(coins)
        if amount == 0:
            return 1
        if i == n:
            return 0
        if dp[i][amount] is not None:
            return dp[i][amount]
        if amount >= coins[i]:
            choose = self.coinChange(i, amount - coins[i], coins, dp)
            not_choose = self.coinChange(i+1, amount, coins, dp)
            dp[i][amount] = choose + not_choose
        else:
            dp[i][amount] = self.coinChange(i+1, amount, coins, dp)
        
        return dp[i][amount]


    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[None for i in range(amount+1)] for j in range(n+1)]
        return self.coinChange(0, amount, coins, dp)