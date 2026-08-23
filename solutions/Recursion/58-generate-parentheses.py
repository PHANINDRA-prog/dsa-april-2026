class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(open_count,close_count,path):
            if open_count == 0 and close_count == 0:
                return [path]
            
            answers = []
            if close_count > open_count:
                pick_close = helper(open_count,close_count - 1,path + ")")
                answers.extend(pick_close)
            
            if open_count > 0:
                pick_open = helper(open_count - 1 , close_count , path + "(")
                answers.extend(pick_open)
            
            return answers
        return helper(n,n,"")