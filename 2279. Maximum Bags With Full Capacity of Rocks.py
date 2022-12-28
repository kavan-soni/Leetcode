class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        remainingCapacity = [capacity[i]-rocks[i] for i in range(len(rocks))]
        remainingCapacity = sorted(remainingCapacity)

        ans = 0

        for x in remainingCapacity:
            if x ==0 : ans+=1; continue;
            if additionalRocks == 0 : break;
            if x <= additionalRocks : additionalRocks -= x; ans+=1;
        
        return ans