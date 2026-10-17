class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        best_buy = float('inf')
        best_sell = 0

        for price in prices:
            if price < best_buy:
                best_buy = price
            
            best_sell = max(best_sell,price - best_buy)
        return best_sell