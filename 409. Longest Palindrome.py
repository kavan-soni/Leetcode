class Solution:
    def longestPalindrome(self, s: str) -> int:

        c = collections.Counter(s)
        print(c)

        answer = 0
        
        odd = False
        for char in c:
            if c[char]%2 == 0: answer+=c[char]
            else: 
                answer+=(c[char] - 1)
                odd = True
        
        return answer+1 if odd else answer

