class Solution:
    def robMoney(self, i: int, nums: list[int], dp: list[int]) -> int:
        n = len(nums)
        if i >= n:
            return 0
        if dp[i] is not None:
            return dp[i]       
        res = max(nums[i] + self.robMoney(i+2, nums, dp), self.robMoney(i+1, nums, dp))
        dp[i] = res
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None] * (n+1)
        return self.robMoney(0, nums, dp)
        