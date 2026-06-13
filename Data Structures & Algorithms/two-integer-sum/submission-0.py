class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            complementary = target - nums[i]
            if complementary in seen:
                return [seen[complementary], i]
            seen[nums[i]] = i
        