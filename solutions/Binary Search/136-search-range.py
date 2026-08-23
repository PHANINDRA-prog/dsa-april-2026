import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx1 = bisect.bisect_left(nums,target)
        
        if idx1 == len(nums) or nums[idx1] != target:
            return [-1,-1]
        
        idx2 = bisect.bisect_right(nums,target)

        return [idx1,idx2-1]