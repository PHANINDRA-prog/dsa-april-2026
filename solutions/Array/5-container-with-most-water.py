// Time Complexity O(n)
// Space Complexity O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        answer = 0

        while left<right:
            area = (right-left)*min(height[left],height[right])
            answer = max(area,answer)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return answer

