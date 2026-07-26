class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def helper(curr_sum):
            if curr_sum == n:
                return 1
            
            if curr_sum > n:
                return 0
            
            total_valid_paths = 0
            step_one = helper(curr_sum + 1)
            total_valid_paths += step_one
            step_two = helper(curr_sum + 2)
            total_valid_paths += step_two
            return total_valid_paths
        return helper(0)