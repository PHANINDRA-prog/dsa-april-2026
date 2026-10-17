class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        
        @cache
        def helper(index,isStartRobbed):

            if index >= n:
                return 0
            

            # Not Pick Case
            notPick = helper(index+1,isStartRobbed)

            # Pick Case
            pick = 0
            if index < n-1 or not isStartRobbed:
                pick = nums[index] + helper(index+2,isStartRobbed or index == 0)
            
            return max(pick,notPick)
        return helper(0,False)