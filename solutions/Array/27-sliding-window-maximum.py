//TC : O(n)
//SC : O(n)
# Now this is simple approach but that max you see will make it worse if it's O(n) and there by boom n2

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         left = 0
#         answer = []
#         for right in range(len(nums)):
#             if (right - left + 1) > k:
#                 left += 1
            
#             if (right - left + 1) == k:
#                 answer.append(max(nums[left:right+1]))
#         return(answer)
        
# Better Approach
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()   # stores indices
        answer = []
        left = 0

        for right in range(len(nums)):

            # Remove smaller elements from back
            # because current element is better
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # Add current index
            dq.append(right)

            # Remove indices outside window
            if dq[0] < left:
                dq.popleft()

            # Window formed
            if (right - left + 1) == k:

                # Front of deque = maximum
                answer.append(nums[dq[0]])

                # Slide window
                left += 1

        return answerck[-1]