class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        count = 0
        minpos = maxpos = leftbound = -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK : leftbound = i
            if nums[i] == minK : minpos = i
            if nums[i] == maxK : maxpos = i
            count += max(0, min(minpos, maxpos) - leftbound)
        
        return count

        
        '''
        # brute force
        count = 0
        for i in range(len(nums)):
            mink, maxk = nums[i], nums[i]
            for j in range(i,len(nums)):
                mink, maxk = min(mink,nums[j]), max(maxk,nums[j])
                if mink < minK or maxk > maxK : break
                if mink == minK and maxk == maxK : count +=1
        return count
        '''