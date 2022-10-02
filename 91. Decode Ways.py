class Solution:
    def numDecodings(self, s: str) -> int:

        def isValid(p,n):
            return 1 if p<len(s)-n+1 and str(int(s[p:p+n]))== s[p:p+n] and 1<=int(s[p:p+n])<=26 else 0
        
        @lru_cache(maxsize=None)
        def decoding(p):
            if p == len(s) : return 1
            if p>len(s) or s[p] == "0": return 0
            return isValid(p,1)*decoding(p+1) + isValid(p,2)*decoding(p+2)

        return decoding(0)