# Brute Force approach 
# Time Complexity for brute force is O(n2) and optimized O(n)
# Space Complexity for brute force O(n) and optimized O(n)

# class Solution:

#     def trap(self, height: List[int]) -> int:

#         n = len(height)

#         answer = 0

#         for i in range(n):

#             left_max = max(height[0:i+1])

#             right_max = max(height[i:n])

#             answer += min(left_max,right_max) - height[i]

#         return answer




# Optimized Approach

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        answer = 0

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        for i in range(n):
            answer += min(left_max[i], right_max[i]) - height[i]

        return answer
