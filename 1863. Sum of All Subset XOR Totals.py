class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        

        def helper(index, xor):
            if index == n: return xor

            with_index = helper(index+1, xor^nums[index])
            without_index = helper(index+1, xor)
            
            return with_index + without_index

        
        n = len(nums)
        return helper(0, 0)