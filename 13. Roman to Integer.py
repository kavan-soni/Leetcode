class Solution:
    def romanToInt(self, s: str) -> int:

        i = 0
        answer = 0
        while i != len(s):

            if  s[i] == "I":
                if i+1!=len(s) and s[i+1] == 'V' : answer += 4; i+=1
                elif i+1!=len(s) and s[i+1] == 'X' : answer += 9; i+=1
                else: answer += 1

            elif  s[i] == "X":
                if i+1!=len(s) and s[i+1] == 'L' : answer += 40; i+=1
                elif i+1!=len(s) and s[i+1] == 'C' : answer += 90; i+=1
                else: answer += 10

            elif  s[i] == "C":
                if i+1!=len(s) and s[i+1] == 'D' : answer += 400; i+=1
                elif i+1!=len(s) and s[i+1] == 'M' : answer += 900; i+=1
                else: answer += 100
            
            elif  s[i] == "V": answer += 5
            elif  s[i] == "L": answer += 50
            elif  s[i] == "D": answer += 500
            elif  s[i] == "M": answer += 1000

            i+=1
        
        return answer