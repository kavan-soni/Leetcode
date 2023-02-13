class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-x for x in stones]
        heapq.heapify(stone)
        
        
        while len(stone)>1:
            a = abs(heappop(stone))
            b = abs(heappop(stone))
            if a - b !=0 : heappush(stone, -abs(a - b))

        return -stone[0] if stone else 0
