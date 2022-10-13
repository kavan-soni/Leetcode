class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        #Triangular inequality A+B>C
        
        nums.sort(reverse=True)
        
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] + nums[i+1]:
                return nums[i-1] + nums[i] + nums[i+1]
        
        return 0