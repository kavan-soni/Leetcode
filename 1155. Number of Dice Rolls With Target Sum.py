class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @lru_cache(maxsize=None)
        def calcways(dice, remainder):
            
            if remainder<=0 : return 0
            if dice == 1 and 0<remainder<=k : return 1
            if dice == 1 and remainder > k : return 0 
            
            ways = 0
            for i in range(1,k+1):
                ways += calcways(dice-1, remainder-i)
            return ways

        return calcways(n,target) % (10**9 + 7) if k*n >= target else 0