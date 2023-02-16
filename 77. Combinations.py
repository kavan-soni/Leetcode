class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = list()

        def helper(arr, index):
            if len(arr) == k: ans.append(arr); return
            for i in range(index+1,n+1):
                helper(arr+[i], i)

        helper([],0)
        return list(ans)