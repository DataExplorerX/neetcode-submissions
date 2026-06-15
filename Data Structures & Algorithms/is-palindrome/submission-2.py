import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # low, high = 0, len(s)-1
        # while low < high:
        #     if s[low] == s[high]:
        #         low+=1
        #         high-=1
        #     else:
        #         return False
        # return True

        low, high = 0, len(s) - 1
        while low < high:
            while low < high and not s[low].isalnum():
                low += 1
            while low < high and not s[high].isalnum():
                high -=1
            if s[low].lower() != s[high].lower():
                return False
            low += 1
            high -= 1
        return True
