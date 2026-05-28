//TC : O(n2)
//SC : O(1)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []
        n = len(nums)
        for i in range(n):
            left = i + 1
            right = n - 1

            if nums[i] == nums[i-1] and i > 0:
                continue
            
            while left < right:
                total = nums[left] + nums[right] + nums[i]

                if total == 0:
                    answer.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < 0 :
                    left += 1
                else:
                    right -= 1
        return answer