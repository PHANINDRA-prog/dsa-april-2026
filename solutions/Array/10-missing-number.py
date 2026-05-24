// Time Complexity O(n)
// Space Complexity O(1)
# This one is using the division and multiplication formula and below one xor both have same time and space complexity
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         total_sum = (n*(n+1))//2
#         actual_sum = sum(nums)
#         return total_sum - actual_sum


# This one is using xor operator
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_sum = 0
        for i in range(1,n+1):
            xor_sum ^= i
        for num in nums:
            xor_sum ^= num
        return xor_sum