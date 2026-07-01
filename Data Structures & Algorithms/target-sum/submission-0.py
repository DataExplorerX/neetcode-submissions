class Solution:
    def targetSumDp(self, i: int, nums: List[int], target: int, dp: List[List[int]], offset: int) -> int:
        n = len(nums)
        if i >= n:
            if target == 0:
                return 1
            return 0

        if dp[i][target + offset] is not None:
            return dp[i][target + offset]

        add = self.targetSumDp(i+1, nums, target - nums[i], dp, offset)
        sub = self.targetSumDp(i+1, nums, target + nums[i], dp, offset)
        dp[i][target + offset] = add + sub
        
        return dp[i][target + offset]
        

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset = sum(nums) + abs(target)
        dp = [[None for _ in range(2*offset+1)] for _ in range(len(nums)+1)]
        return self.targetSumDp(0, nums, target, dp, offset)

        