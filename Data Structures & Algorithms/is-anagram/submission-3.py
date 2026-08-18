from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charcount = defaultdict(int)

        for i in range(len(s)):
            charcount[s[i]] += 1
            charcount[t[i]] -= 1

        for c in charcount.values():
            if c != 0:
                return False

        return True