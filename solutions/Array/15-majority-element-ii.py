// TC : O(n)
// SC : O(1)
from collections import Counter
import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand_one = None
        cand_two = None
        cand_one_count = 0
        cand_two_count = 0

        for i in range(len(nums)):
            if nums[i]== cand_one:
                cand_one_count += 1
            elif nums[i]== cand_two:
                cand_two_count += 1
            elif cand_one_count == 0:
                cand_one = nums[i]
                cand_one_count = 1
            elif cand_two_count == 0:
                cand_two = nums[i]
                cand_two_count = 1
            else:
                cand_one_count -=1 
                cand_two_count -=1
        count_1 = 0
        count_2 = 0
        for num in nums:
            if num == cand_one:
                count_1 += 1
            elif num == cand_two:
                count_2 += 1
        result = []
        if count_1 > len(nums)//3:
            result.append(cand_one)
        if count_2 > len(nums)//3:
            result.append(cand_two)
        return result
            