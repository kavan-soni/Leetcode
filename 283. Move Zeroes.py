class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while n !=0:
            if nums[i] ==0 :
                nums.append(0)
                del(nums[i])
            else: i+=1

            n-=1
        