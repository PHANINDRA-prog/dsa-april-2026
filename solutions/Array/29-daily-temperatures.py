//TC : O(n)
//SC : O(n)

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temp)
        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                past_day = stack.pop()
                res[past_day] = i - past_day
            
            stack.append(i)
        return res
        