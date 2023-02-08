class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        ans = []
        
        for num in c1 :
            if num in c2:
                ans += [num] * min(c1[num],c2[num])
        return ans