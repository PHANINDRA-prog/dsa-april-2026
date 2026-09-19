from functools import cache
class Solution:
    def totalWays(self, nums: list[int], target: int) -> int:
        # code here
        @cache
        def helper(index,curr_sum):
            if index == len(nums):
                if curr_sum == target:
                    return 1
                return 0


            plus = helper(index + 1,curr_sum + nums[index])
            minus = helper(index + 1,curr_sum - nums[index])
            return plus + minus
        return helper(0,0)