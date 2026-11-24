class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        
        while low <= high:
            mid = (low + high)//2

            hrs = 0
            for i in piles:
                hrs += (i + mid - 1) // mid
            
            if hrs <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

        