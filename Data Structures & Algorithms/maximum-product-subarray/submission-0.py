class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxDP = [None]*n
        minDP = [None]*n

        def solve(i):
            if i == 0:
                maxDP[i] = nums[i]
                minDP[i] = nums[i]

                return maxDP[i]
            
            if maxDP[i] is not None:
                return maxDP[i]
            
            prevMax = solve(i-1)
            prevMin = minDP[i-1]

            maxDP[i] = max(nums[i], nums[i] * prevMax, nums[i] * prevMin)
            minDP[i] = min(nums[i], nums[i] * prevMax, nums[i] * prevMin)

            return maxDP[i]
        
        ans = float('-inf')

        for i in range(n):
            ans = max(ans, solve(i))
        
        return ans
        