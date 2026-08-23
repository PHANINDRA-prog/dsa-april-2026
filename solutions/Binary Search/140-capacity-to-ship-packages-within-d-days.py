class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(capacity):

            number_of_days = 1
            current_capacity = 0

            for num in weights:
                if current_capacity + num <= capacity:
                    current_capacity += num
                
                else:
                    number_of_days +=1
                    current_capacity = num
            
            return number_of_days <= days
        
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right)//2

            if check(mid):
                right = mid
            
            else:
                left = mid + 1
        return left