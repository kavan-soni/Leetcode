class Solution:
    def fillCups(self, amount: List[int]) -> int:
        time = 0
        heap = [-num for num in amount if num !=0]

        while heap:
            
            if len(heap) == 1: return time + (-heappop(heap))
            
            x, y  = -heappop(heap), -heappop(heap)
            
            x -=1
            if x: heappush(heap, -x)

            y -=1
            if y: heappush(heap, -y)
            
            time +=1 
        
        return time