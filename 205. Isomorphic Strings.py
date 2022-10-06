class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        d = {}

        for i,v in enumerate(s):
            if not v in d.keys():
                if t[i] not in d.values():
                    d[v] = t[i]
                    continue
                else: return False
            elif v in d.keys() and d[v] != t[i]: return False
        
        return True


    """
    # One line solution
    class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))
    """