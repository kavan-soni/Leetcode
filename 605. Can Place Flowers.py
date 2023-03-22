class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:

        ans = 0
        nums.insert(0,0)
        nums.append(0)

        for i in range(1,len(nums)-1) :
            if nums[i] == 0 and nums[i-1] == 0 and nums[i+1] == 0 :
                    nums[i] = 1
                    n -= 1
            if n <= 0 : return True
        
        return False