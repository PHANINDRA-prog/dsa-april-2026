class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(speed):
            total_time = 0

            for pile in piles:
                total_time += ceil(pile/speed)

            return total_time <= h
        
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right)//2

            if check(mid):
                right = mid
            
            else:
                left = mid + 1
        return left