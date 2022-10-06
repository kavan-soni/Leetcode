import collections
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s)>len(t): return False
        p = 0

        for i in range(len(s)):
            if p > len(t)-1: return False
            while t[p]!=s[i]:
                p +=1
                if p > len(t)-1: return False
            p+=1
            
        return True