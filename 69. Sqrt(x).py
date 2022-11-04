class Solution:
    def mySqrt(self, x: int) -> int:

        if x <=1: return x
        
        answer = 1
        for i in range(1, x//2 + 1):
            if i*i <= x: answer = i
            else: break
        return answer