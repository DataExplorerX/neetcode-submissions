class Solution:
    def power(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n % 2 == 0:
            n = n//2
            x = x * x
            return self.power(x, n)
        else:
            new_n = n - 1
            return x * self.power(x, new_n)
        

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.power(x, abs(n))
        return self.power(x, n)
        