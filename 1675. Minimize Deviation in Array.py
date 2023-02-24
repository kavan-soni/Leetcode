class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        curr_min = -1000000001
        min_deviation = 1000000001
        
        pq = []
        for num in nums:
            if num % 2 : num *= -2
            else: num *= -1
            pq.append(num)
            curr_min = max(num, curr_min)
        
        heapq.heapify(pq)

        while pq :
            curr_max = heapq.heappop(pq)
            min_deviation = min(abs(curr_max - curr_min), min_deviation)
            #print(curr_max, curr_min, pq, min_deviation)
            if curr_max % 2 : break # maximum element is odd
            curr_max //= 2
            curr_min = max(curr_min, curr_max)
            heapq.heappush(pq, curr_max)
        
        return min_deviation
            