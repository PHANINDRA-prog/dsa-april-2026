class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)

        @cache
        def helper(day,holding):
            if day == n:
                return 0
            
            if holding == 0:
                rest = helper(day +1 ,0)

                buy = -prices[day] + helper(day + 1,1)

                return max(rest,buy)
            
            else:

                rest = helper(day+1,1)

                sell = prices[day] + helper(day + 1,0)

                return max(rest,sell)
            
        return helper(0,0)