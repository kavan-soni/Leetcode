class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        max_dist = 0

        for i, num in enumerate(nums1): 
            l, r = 0, len(nums2)
            while l<r :
                m = l + (r-l)//2
                if num > nums2[m] : r = m
                else: l = m + 1
            max_dist = max(max_dist, l-1 - i)
        
        return max_dist

            
            