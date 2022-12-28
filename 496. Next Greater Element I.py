class Solution:
    # do all
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []     
        d =  {}
        for num in nums2 :
            while stack and num > stack[-1]:
                d[stack.pop()] = num
            stack.append(num)

        return [d.get(num, -1) for num in nums1 ]
            
        '''
        ans = []
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            ans.append(-1)
            for k in nums2[min(j+1,len(nums2)-1):len(nums2)]:
                if k > nums2[j] : 
                    ans[-1] = k
                    break
        return ans
        '''
                    
            