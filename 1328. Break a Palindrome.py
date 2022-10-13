class Solution:
    def breakPalindrome(self, P: str) -> str:
        
        for i in range(len(P)//2):
            if P[i] != 'a': return P[:i]+'a'+P[i+1:]
        return P[:-1]+'b' if len(P) > 1 else ''


