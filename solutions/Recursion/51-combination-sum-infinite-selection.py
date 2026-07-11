class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # Top Down Approach
        def helper(index,curr_sum,path):
            if index == len(candidates):
                if curr_sum == target:
                    return [path]
                return []
            
            if curr_sum > target:
                return []
            
            answers = []
            next_sum = curr_sum + candidates[index]
            child = helper(index,next_sum,path + [candidates[index]]) # Pick the same number
            answers.extend(child)

            next_sum = curr_sum
            child = helper(index+1,next_sum,path) # Picking the different Number

            answers.extend(child)
            return answers
        return helper(0,0,[])


        # Bottom Up Approach
        def helper(index,target):
            if target == 0:
                return [[]]
            
            if index == len(candidates):
                return []
            
            answer = []

            if candidates[index] <= target:
                take = helper(index,target - candidates[index])

                for bag in take:
                    answer.append([candidates[index]] + bag)
                
            skip = helper(index+1,target)
            
            for bag in skip:
                answer.append(bag)
                
            return answer
        return helper(0,target)