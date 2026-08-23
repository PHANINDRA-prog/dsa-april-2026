class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # This algo is all about finding the sorted half and searching the element in the sorted half

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            
            # Adding that check because when both mid and left point to same element that case also we need to cover
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

