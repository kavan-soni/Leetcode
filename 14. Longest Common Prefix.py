class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def commonPrefix(s1, s2):
            i = 0
            while i< min(len(s1), len(s2)):
                if s1[i]!=s2[i]: return s1[:i]
                i+=1
            return s1 if len(s1)<len(s2) else s2

        prev = strs[0]
        answer = prev
        for s in strs:
            curr = commonPrefix(prev, s)
            answer = commonPrefix(answer, curr)
        return answer


