class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs = sorted(costs)

        for idx, cost in enumerate(costs):
            if cost <= coins: coins -= cost    
            else: return idx
        return len(costs)



