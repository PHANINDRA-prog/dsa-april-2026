//TC : O(nlogk)
//SC : O(1)

from collections import Counter
import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)

        top_two = heapq.nlargest(2, (item for item in counts.items() if item[1] > n/3), key=lambda item: item[1])
        result = [item[0] for item in top_two]
        return result
        