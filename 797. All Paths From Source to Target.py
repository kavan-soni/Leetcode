class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1
        ans = []
        
        def dfs(node, arr):
            arr1 = arr.copy()
            arr1.append(node)

            if node == n: #basecase
                ans.append(arr1)
                return

            for neighbor in graph[node]:
                dfs(neighbor, arr1)

            

        dfs(0,[])
        return ans



        


