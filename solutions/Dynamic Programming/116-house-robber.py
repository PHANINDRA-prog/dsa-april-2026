class Solution:
    def rob(self, nums: list[int]) -> int:
        
        n = len(nums)
        @cache
        def helper(i):
            if i >= n:
                return 0
            
            notPick = helper(i+1)

            pick = nums[i] + helper(i+2)
            
            return max(pick , notPick)
        return helper(0)
    