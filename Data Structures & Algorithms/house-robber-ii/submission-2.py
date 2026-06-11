class Solution:
    def houseRob(self, i: int, nums: list[int], dp: list[int]) -> int:
        n = len(nums)
        if i >= n:
            return 0
        if dp[i] is not None:
            return dp[i]
        moveNextHouse = self.houseRob(i+1, nums, dp)
        chooseHouse = nums[i] + self.houseRob(i+2, nums, dp)
        dp[i] = max(moveNextHouse, chooseHouse)
        return dp[i]
    
    def solve(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [None] * n
        return self.houseRob(0, nums, dp)


    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.solve(nums[:-1]), self.solve(nums[1:]))