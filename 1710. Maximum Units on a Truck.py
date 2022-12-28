class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        total = 0

        for [x,y] in boxTypes:
            if truckSize >= x : 
                total += x*y
                truckSize -= x
            else:
                total += truckSize*y
                break
        return total
