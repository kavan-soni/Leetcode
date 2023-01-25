class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        def helper(arr):
            
            if sum(arr) > target : return
            
            if sum(arr) == target : 
                if (x:=sorted(arr)) not in ans: ans.append(x)
                return

            for i in range(len(candidates)):
                helper(arr + [candidates[i]])

        helper([])
        return ans
