class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)

        for num in c:
            if c[num] > len(nums)//2: return num