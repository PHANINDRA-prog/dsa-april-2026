class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def targetSum(index,curr_sum):
            if index == len(nums):
                if curr_sum == target:
                    return True
                return False
            
            if (index,curr_sum) in memo:
                return memo[(index,curr_sum)]
            next_sum = curr_sum + nums[index]
            plus = targetSum(index+1,next_sum)
            

            next_sum = curr_sum - nums[index]
            minus = targetSum(index+1,next_sum)
            
            memo[(index,curr_sum)] = plus or minus
            return plus or minus
        return (targetSum(0,0))

