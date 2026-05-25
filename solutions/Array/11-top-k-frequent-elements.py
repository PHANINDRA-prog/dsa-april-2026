from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        top_k = heapq.nlargest(k,count.items(),key = lambda item:item[1])

        result = [item[0] for item in top_k]

        return result