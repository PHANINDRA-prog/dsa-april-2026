//TC : O(n)
//SC : O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reversed(start,end):
            left = start
            right = end
            while left <= right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        
        reversed(0,n-1)
        reversed(0,k-1)
        reversed(k,n-1)