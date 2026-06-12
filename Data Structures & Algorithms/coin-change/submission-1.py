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
        dp = [[float('inf') for _ in range(amount+2)] for _ in range(len(coins)+2)]
        # res = self.coinChangedp(0, coins, amount, dp)
        # return res if res != float('inf') else -1

        for i in range(len(coins) + 2):
            dp[i][0] = 0
        for j in range(1, amount+2):
            dp[len(coins)+1][j] = float('inf')
        
        for i in range(len(coins)-1, -1, -1):
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    choose = 1 + dp[i][j - coins[i]]
                    not_choose = dp[i+1][j]
                    dp[i][j] = min(choose, not_choose)
                else:
                    dp[i][j] = dp[i+1][j]
        if(dp[0][amount]) != float('inf'):
            return dp[0][amount]
        return -1



        