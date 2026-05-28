//TC : O(nlogn)
//SC : O(1)
# This is more a naive approach of using two sums to find all pairs
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         left = 0
#         right = len(nums) - 1
#         count = 0
#         while left < right:
#             total = nums[left] + nums[right]

#             if total < k :
#                 left += 1
#             elif total > k:
#                 right -= 1
#             else:
#                 count += 1
#                 left += 1
#                 right -= 1
#         return count

#Hash map approach reducing it to O(n)
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = {}  # Acts as a waiting room for numbers
        operations = 0

        for num in nums:
            complement = k - num

            # Check if the perfect partner is already waiting in the room
            if seen.get(complement, 0) > 0:
                operations += 1
                seen[complement] -= 1  # Pair found! Consume the partner
            else:
                # No partner waiting? Add current number to the room
                seen[num] = seen.get(num, 0) + 1

        return operations
