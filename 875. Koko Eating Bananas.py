class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canFinish(rate):
            total_hours_needed = 0

            for pile in piles:
                hours_to_eat_pile = math.ceil(pile/rate)
                total_hours_needed += hours_to_eat_pile
                if total_hours_needed > h : return False

            return True

        l = 1 # min possible value of k(rate) when h tends to infinity
        r = max(piles) # max possible value of k(rate) when h = len(piles)

        while l < r :
            m = l + (r-l)//2
            if canFinish(m): r = m
            else: l = m+1
        return l

