import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k==1: return nums

        dq = collections.deque([],maxlen=k)
        ans = []


        for i in range(k):
            while dq and dq[-1]<nums[i]:
                dq.pop()
            dq.append(nums[i])
        
        ans.append(dq[0])

        for i in range(k,len(nums)):
            while dq and dq[-1]<nums[i]:
                dq.pop()
            dq.append(nums[i])
            if len(dq)<k and nums[i-k+1] == dq[0]: dq.popleft()
            ans.append(dq[0])
            
        return ans
