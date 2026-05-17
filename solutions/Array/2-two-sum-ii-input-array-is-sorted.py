//TC : O(n)
//SC : O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        while left < right :
            total_sum = numbers[left] + numbers[right]
            if total_sum == target:
                return [left+1,right+1]
            elif total_sum < target:
                left += 1
            else:
                right -= 1