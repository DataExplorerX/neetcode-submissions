class Solution:
    def coinChangedp(self, i: int, coins: list[int], amount: int, dp: list[list[int]]) -> int:
        n = len(coins)
        if amount == 0:
            return 0
        if i >= n and amount != 0:
            return float('inf')

        if dp[i][amount] is not None:
            return dp[i][amount]
        
        if coins[i] <= amount:
            choose = 1 + self.coinChangedp(i, coins, amount - coins[i], dp)
            not_choose = self.coinChangedp(i+1, coins, amount, dp)
            dp[i][amount] = min(choose, not_choose)

        else:
            dp[i][amount] = self.coinChangedp(i+1, coins, amount, dp)

        return dp[i][amount]


    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[None for _ in range(amount+1)] for _ in range(len(coins)+1)]
        res = self.coinChangedp(0, coins, amount, dp)
        return res if res != float('inf') else -1

        