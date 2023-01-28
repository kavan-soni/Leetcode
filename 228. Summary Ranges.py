class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        nums = list([x,x] for x in nums)

        ans = []

        while nums:
            num = nums.pop(0)
            if not ans: ans.append(num); continue

            if ans[-1][1] + 1 >= num[0]:
                ans[-1][0] = min(ans[-1][0], num[0])
                ans[-1][1] = max(ans[-1][1], num[1])
            else:
                ans.append(num)
        
        
        genAns = lambda a,b : str(a) if a == b else str(a)+"->"+str(b)
        
        return [genAns(a,b) for a,b in ans]

