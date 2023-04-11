class Solution:
    def partitionString(self, s: str) -> int:
        
        ans, curr = 1, ""

        for i in range(len(s)):
            if s[i] not in curr :
                curr += s[i]
            else:
                ans += 1
                curr = s[i]
        
        return ans
