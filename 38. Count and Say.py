class Solution:
    def countAndSay(self, n: int) -> str:

        def helper(k):
            if k == 1: return "1"
            s = helper(k-1)

            prev = s[0]
            count = 0
            i=0
            ds = ""

            while i <= len(s):
                if i == len(s): ds += str(count) + str(prev)
                elif s[i] == prev: count +=1
                else:
                    ds += str(count) + str(prev)
                    prev = s[i]
                    count = 1
                i +=1

            return ds
        
        return helper(n)