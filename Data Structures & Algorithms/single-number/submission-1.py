class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # seen = {}
        # ans = 0
        # for i in nums:
        #     if i not in seen:
        #         seen[i] = 1
        #     else:
        #         seen[i] += 1
        # for key, val in seen.items():
        #     if val == 1:
        #         ans = key
        # return ans

        ans = 0
        for i in nums:
            ans ^= i
        return ans