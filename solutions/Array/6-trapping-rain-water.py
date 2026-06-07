// TC : O(n)
// SC : O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        # Prefix and Suffix Approach
        # n = len(height)
        # left_max = [0]*n
        # right_max = [0]*n

        # left_max[0] = height[0]
        # for i in range(1,len(height)):
        #     left_max[i] = max(left_max[i-1],height[i])
        
        # right_max[n-1] = height[n-1]
        # for i in range(n-2,-1,-1):
        #     right_max[i] = max(right_max[i+1],height[i])
        
        # answer = 0
        # for i in range(n):
        #     answer += min(left_max[i],right_max[i]) - height[i]
        # return answer

        # Now Greedy Approach
        n = len(height)
        left = 0
        right = n - 1
        left_max = height[left]
        right_max = height[right]
        answer = 0
        while left<right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max,height[left])
                answer += left_max - height[left]
            
            else:
                right -= 1
                right_max = max(right_max,height[right])
                answer += right_max - height[right]
        return answer