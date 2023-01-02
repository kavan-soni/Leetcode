class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()
        if len(s) != len(pattern) : return False
        d = collections.defaultdict(str)
        
        for i in range(len(pattern)):
            if pattern[i] in d:
                if s[i] != d[pattern[i]]: return False

            else:
                d[pattern[i]] = s[i]
        return True if len(set(d.values())) ==  len(d.values()) else False
        