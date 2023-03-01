class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans = []
        heapq.heapify(nums)
        while nums:
            num = heapq.heappop(nums)
            ans.append(num)
        return ans
