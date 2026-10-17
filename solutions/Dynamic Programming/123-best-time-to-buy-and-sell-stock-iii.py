class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        if not prices:
            return 0
        
        n = len(prices)

        @cache
        def helper(day,holding,cap):
            if day == n or cap == 0:
                return 0
            
            if holding == 0:
                rest = helper(day +1 ,0,cap)

                buy = -prices[day] + helper(day + 1,1,cap)

                return max(rest,buy)
            
            else:

                rest = helper(day+1,1,cap)

                sell = prices[day] + helper(day + 1,0,cap -1)

                return max(rest,sell)
            
        return helper(0,0,2)