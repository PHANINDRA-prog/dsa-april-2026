//TC : O(n)
//SC : O(1)

# Normal Approach for a singular s
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i = 0
#         j = 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
        
#         return i == len(s)

# For many s first preprocess s and then by being greedy take the smallest valid position > previous and once this satisfies then we are good

from collections import defaultdict
import bisect

class Solution:

    def isSubsequence(self,s,t):

        from collections import defaultdict
        import bisect

        positions = defaultdict(list)

        for i,char in enumerate(t):

            positions[char].append(i)

        prev = -1

        for char in s:

            if char not in positions:
                return False

            arr = positions[char]

            idx = bisect.bisect_right(
                arr,
                prev
            )

            if idx == len(arr):
                return False

            prev = arr[idx]

        return True