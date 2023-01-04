class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)

        d = collections.defaultdict(bool)

        def jump(idx):

            if idx in d: 
                return d[idx]

            if idx == n-1 : 
                d[idx] = True
                return True

            for i in range( min(n-1, idx + nums[idx]), idx, -1):
                
                if jump(i) : 
                    d[idx] = True
                    return True
            
            d[idx] = False
            return False



        return jump(0)