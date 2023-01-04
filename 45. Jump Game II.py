class Solution:
    def jump(self, nums: List[int]) -> int:

        d = collections.defaultdict(int)
        n = len(nums)

        def jump(idx):

            if idx in d : return d[idx]
            if idx == n-1 : return 0

            min_jumps = 100000

            for i in range(min(n-1, idx+nums[idx]), idx, -1):
                min_jumps = min(min_jumps, 1 + jump(i))

            d[idx] = min_jumps
            return min_jumps


        return jump(0)
