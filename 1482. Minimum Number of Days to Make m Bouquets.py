class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        n = len(bloomDay)
        if m*k > n: return -1

        #print(bloomDay)

        # bloomDay[i] -> day when flower i blooms
        # m -> total number of bouquets required
        # k -> number of adjacent flowers to use -> subarray size

        def bloomed(arr, day):
            #print("moose", day, arr, all([ day >= d and d!= -1 for d in arr]) and len(arr) == k)
            return len(arr) == k and all([ day >= d for d in arr])


        def feasible(day):
            bouquet = []
            temp = bloomDay
            i=0

            while 0<=i<n:
                if bloomed(temp[i:i+k], day): 
                    bouquet.append(i)
                    #temp = temp[:i] + [1000000001] * k + temp[i+k:]
                    #print("wala", day, i, temp, len(bouquet), m, len(bouquet) >= m)
                else:  i = i-k+1
                
                if len(bouquet) >= m: return True
                i += k

            return False

        l = min(bloomDay) # min days to wait = 1 if flowers bloom on day1
        r = max(bloomDay) # max days to wait = max(bloomDay) if all flowers bloom on last day

        while l<r:
            mid = l + (r-l)//2
            #print("sidhu", l, r, mid)
            if feasible(mid): r = mid
            else: l = mid+1
        return l
