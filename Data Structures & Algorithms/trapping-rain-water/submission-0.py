class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pmax = [0]*n
        smax = [0]*n
        ans = 0
        pmax[0] = height[0]
        smax[n-1] = height[n-1]

        for i in range(1,n):
            pmax[i] = max(height[i], pmax[i-1])
        for i in range(n-2, -1, -1):
            smax[i] = max(height[i], smax[i+1])
        
        for i in range(1, n-1):
            ans += min(pmax[i], smax[i]) - height[i]
        
        return ans

        