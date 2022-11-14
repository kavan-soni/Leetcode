class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        dp  = [-1]*n

        def helper(i):
            
            if [i,destination] in edges or [destination,i] in edges: return True
            
            l = []
            
            for edge in edges:
                if i in edge:
                    if edge[0] == i: temp = edge[1]
                    else: temp = edge[0]
                    if dp[temp] == 1:
                        dp[i] = True
                        return True
                    if dp[temp] == -1: l.append(temp)
            
            ans = False
            for node in l:
                dp[node] = -2
                ans |= helper(node)
                if ans: 
                    dp[node] = 1
                    return ans
            return ans
            
        return True if n ==1 else helper(source)
