class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)

        y=len(nums)-1

        diff = float('inf')

        for i in range(0,len(nums)-2):
            j = i+1
            k = len(nums)-1

            while j<k:
                sum_ = nums[i]+nums[j]+nums[k]
                if sum_ == target : return sum_
                elif sum_<target : j+=1
                else: k-=1
                if abs(sum_-target) < diff : 
                    diff = abs(sum_-target)
                    closest = sum_
        return closest