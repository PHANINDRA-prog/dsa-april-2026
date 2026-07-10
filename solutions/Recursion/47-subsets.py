class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Top Down Approach

        def helper(path,index):
            if index == len(nums):
                return [path]
            
            answers = []
            pick = helper(path+[nums[index]],index+1)
            answers.extend(pick)
            notPick = helper(path,index+1)
            answers.extend(notPick)
            return answers
        return helper([],0)


        # Bottom Up Approach

        def helper(index):
            if index == len(nums):
                return [[]]
            
            answers = []
            childBag = helper(index+1)

            for child in childBag:
                # Pick Case
                answers.append(child+[nums[index]])
                # Not Pick Case
                answers.append(child)
            return answers
        return helper(0)