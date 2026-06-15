import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        low, high = 0, len(s)-1
        while low < high:
            if s[low] == s[high]:
                low+=1
                high-=1
            else:
                return False
        return True
