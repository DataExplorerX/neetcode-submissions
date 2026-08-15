class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        partsum = total // 2
        dp = [False] * (partsum + 1)
        dp[0] = True

        for i in nums:
            for s in range(partsum, i - 1, -1):
                dp[s] = dp[s] or dp[s-i]
        return dp[partsum]        