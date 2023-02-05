class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        c1 = collections.Counter(p)
        n = len(p)
        for i in range(len(s)-n+1):
            if collections.Counter(s[i:i+n]) == c1: ans.append(i)
        return ans