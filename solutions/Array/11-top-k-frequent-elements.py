// TC : O(n)
// SC : O(n)
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force Approach n^2
        # frequency_count = Counter(nums)
        # result = []

        # for _ in range(k):
        #     max_elem = None
        #     max_count = -1

        #     for key,value in frequency_count.items():
        #         if value > max_count:
        #             max_count = value
        #             max_elem = key
        #     result.append(max_elem)
        #     del frequency_count[max_elem]
        # return result


        # n log n approach
        # frequency_count = Counter(nums)

        # sorted_keys = sorted(frequency_count, key=frequency_count.get, reverse=True)
        # return sorted_keys[:k]


        # Optimized Approach
        frequency_count = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        for key,value in frequency_count.items():
            buckets[value].append(key)
        
        result = []
        for i in range(n,-1,-1):
            result.extend(buckets[i])
            if len(result) == k:
                return result

