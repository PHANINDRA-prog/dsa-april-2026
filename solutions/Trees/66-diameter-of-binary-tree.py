# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return (0,0)
            
            left_extend,left_solved = helper(node.left)
            right_extend,right_solved = helper(node.right)

            my_extend = 1 + max(left_extend,right_extend)

            through_me = left_extend + right_extend

            my_solved = max(left_solved,right_solved,through_me)

            return (my_extend,my_solved)
        height,answer = helper(root)
        return answer