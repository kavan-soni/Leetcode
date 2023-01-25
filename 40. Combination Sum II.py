class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < min(candidates) or sum(candidates) < target: return []
        
        def helper(index, comb, curr_sum):
            #print(index, curr_sum, comb)
            #if curr_sum > target: return
            if curr_sum == target: 
                if (x:=sorted(comb)) not in ans: ans.append(x)
                #ans.append(comb)
                return
            #if index >= n: return
            

            for i in range(index,n):
                if i > index and candidates[i] == candidates[i-1]: continue
                if curr_sum + candidates[i] > target : break
                helper(i+1, comb + [candidates[i]], curr_sum + candidates[i])
            
        
        ans = list()
        candidates = sorted(candidates)
        n = len(candidates)
        helper(0, [], 0)
        return ans

