class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        l, r = 0, len(arr)-1

        def condition(idx):
            return arr[idx]> arr[idx+1]
        
        while l < r:
            m = l + (r-l)//2
            if condition(m): r = m
            else: l = m+1
        return l