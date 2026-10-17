class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        n = len(coins)
        @cache
        def helper(i,rem_amount):

            if i == n:
                if rem_amount == 0:
                    return 0
                return float('inf')
            

            # Not Take Case
            notTake = helper(i+1,rem_amount)

            # Take Case
            take = float('inf')
            if coins[i] <= rem_amount:
                take = 1+ helper(i,rem_amount - coins[i])
            
            return min(take,notTake)
        result =  helper(0,amount)
        return result if result != float('inf') else -1
            