class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        '''
        #brute-force
        ans = [0]*len(temp)
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                if temp[j]>temp[i] : 
                    ans[i] = j-i
                    break
        return ans
        '''

        stack = []
        ans = [0] * len(temp)

        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                t = stack.pop()
                ans[t] = i - t
            stack.append(i)
        
        return ans
            

        
        