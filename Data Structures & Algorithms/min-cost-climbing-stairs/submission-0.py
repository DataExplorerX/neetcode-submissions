class Solution:
    def costClimbingStairs(self, i: int, cost: list[int], dp: list[int]) -> int:
        n = len(cost)
        if i >= n:
            return 0
        if dp[i] != None:
            return dp[i]
        dp[i] = cost[i] + min(self.costClimbingStairs(i+1, cost, dp), self.costClimbingStairs(i+2, cost, dp))
        return dp[i]


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [None] * n
        return min(self.costClimbingStairs(0, cost, dp), self.costClimbingStairs(1, cost, dp))

        