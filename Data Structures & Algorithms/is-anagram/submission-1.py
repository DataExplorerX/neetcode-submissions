from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # TC - o(nlogn + mlogm) as sorted func does timsort and SC - o(n+m) as we are using "".join creating a new str and storng in s and t -- extra memory propotional to the size of inputs
        # s = "".join(sorted(s))
        # t = "".join(sorted(t))
        # if s == t:
        #     return True
        # return False

        # TC - o(n+m) and SC - o(1)
        if len(s) != len(t):
            return False
        if Counter(s) != Counter(t):
            return False
        return True


