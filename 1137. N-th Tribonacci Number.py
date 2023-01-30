class Solution:
    def tribonacci(self, n: int) -> int:

        dp = collections.defaultdict(int)
        dp[0], dp[1], dp[2] = 0, 1, 1

        def helper(num):
            if num in dp: return dp[num]
            dp[num] = helper(num-1) + helper(num-2) + helper(num-3)
            return dp[num]
       
        return helper(n)