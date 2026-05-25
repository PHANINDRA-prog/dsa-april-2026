//TC : O(nlogk)
//SC : O(1)

from collections import Counter
import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)

        top_one = heapq.nlargest(1,counts.items(), key = lambda item:item[1])
        return top_one[0][0]