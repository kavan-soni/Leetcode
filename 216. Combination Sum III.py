class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        if k *(k+1)/2 > n: return []

        ans = []

        def helper(num, arr):
            if num > 10 or len(arr) > k or sum(arr) > n :  return
            if len(arr) == k and sum(arr) == n :
                ans.append(arr)
                return
            
            helper(num+1, arr + [num])
            helper(num+1, arr)
            

        helper(1, [])
        return ans