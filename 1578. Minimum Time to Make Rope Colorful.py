class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        l = r = 0
        ans = 0

        while r<len(colors):
            while r<len(colors) and colors[l] == colors[r] : r+=1
            if r-l >1 : ans += sum( sorted(neededTime[l:r])[:r-l-1] )
            l=r
            
        return ans