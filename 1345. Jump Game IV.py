class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = defaultdict(list)
        for i, num in enumerate(arr):
            d[num].append(i)

        '''
        dp = defaultdict(int)
        dp[n-1] = 0

        evaluating = set()

        def helper(idx):
            print(idx)
            if idx in dp : return dp[idx]
            if idx in evaluating or idx < 0 or idx >= n : return 500000
            
            evaluating.add(idx)

            temp = 500000
            for x in d[arr[idx]]:
                if x in evaluating or x == idx : continue
                temp = min(temp, helper(x))
            dp[idx] = 1 + min(temp, helper(idx+1), helper(idx-1))

            evaluating.remove(idx)

            return dp[idx]
            
        return helper(0)
        '''

        pq = [(0,0)] #(cost, idx)
        heapq.heapify(pq)
        visited_idx = set()
        visited_value = set()
        while pq:

            cost, idx = heapq.heappop(pq)
            if idx < 0 or idx >= n : continue
            if idx == n-1 : return cost

            visited_idx.add(idx)

            if idx-1 not in visited_idx : heapq.heappush(pq, (cost+1, idx-1))
            if idx+1 not in visited_idx : heapq.heappush(pq, (cost+1, idx+1))
            
            if arr[idx] in visited_value : continue
            for x in d[arr[idx]] :
                if x not in visited_idx : heapq.heappush(pq, (cost+1, x))
            visited_value.add(arr[idx])

        return 0