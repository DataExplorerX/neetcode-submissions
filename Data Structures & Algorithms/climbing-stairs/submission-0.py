class Solution:
    def totalWays(self, i: int, n:int, arr: list[int]) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        if arr[i] is not None:
            return arr[i]
        arr[i] = self.totalWays(i+1, n, arr) + self.totalWays(i+2, n, arr)
        return arr[i]

    def climbStairs(self, n: int) -> int:
        arr = [None] * (n+1)
        return self.totalWays(0, n, arr)
        