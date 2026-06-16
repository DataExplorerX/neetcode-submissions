class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(str(i) for i in digits)
        s = str(int(s) + 1)
        return [int(i) for i in s]
        