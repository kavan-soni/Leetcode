class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        cs, ct = Counter(s), Counter(t)

        for x in ct:
            if x not in cs: return x
            if cs[x] != ct[x] : return x

        


        
        