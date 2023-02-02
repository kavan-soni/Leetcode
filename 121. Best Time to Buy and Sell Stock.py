class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        buy_price = prices[0]

        for price in prices:
            
            profit = max(price - buy_price, profit)
            if price < buy_price: buy_price = price
        return profit