// TC : O(n)
// SC : O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute Force approach of calculating previous smaller and next smaller element
        # def pse(arr):
        #     stack = []
        #     left = [-1] * len(arr)
        #     for i in range(len(arr)):
        #         while stack and arr[stack[-1]] >= arr[i]:
        #             stack.pop()
        #         if stack:
        #             left[i] = stack[-1]
        #         stack.append(i)
        #     return left
        
        # def nse(arr):
        #     stack = []
        #     right = [len(arr)]*len(arr)
        #     for i in range(len(arr)-1,-1,-1):
        #         while stack and arr[stack[-1]] >= arr[i]:
        #             stack.pop()
        #         if stack:
        #             right[i] = stack[-1]
        #         stack.append(i)
        #     return right
        
        # left = pse(heights)
        # right = nse(heights)
        # max_area = 0

        # for i in range(len(heights)):
        #     width = right[i]-left[i]-1
        #     area = heights[i] * width
        #     max_area = max(area,max_area)
        # return max_area

        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                current = stack.pop()
                height = heights[current]

                if stack:
                    left = stack[-1]
                else:
                    left = -1
                
                right = i
                width = right - left - 1
                area = width * height
                max_area = max(max_area,area)
            stack.append(i)
        
        while stack:
            current = stack.pop()
            height = heights[current]

            if stack:
                left = stack[-1]
            else:
                left = -1

            right = len(heights)
            width = right - left - 1
            area = height * width
            max_area = max(max_area,area)
        return max_area