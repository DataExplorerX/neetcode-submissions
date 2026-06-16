class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            new_n = 0
            for i in str(n):
                new_n += int(i) * int(i)
            n = new_n
        return True
        