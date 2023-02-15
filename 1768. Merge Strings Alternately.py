class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        while word1 and word2:
            ans.append(word1[0])
            ans.append(word2[0])
            word1 = word1[1:]
            word2 = word2[1:]
        
        if word1: ans.append(word1)
        if word2: ans.append(word2)
        return "".join(ans)
