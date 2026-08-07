# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):
            if not node:
                return None
            
            # Two children case
            if node.left and node.right:
                node.left,node.right = node.right,node.left
            
            # One children case
            if not node.right:
                node.right = node.left
                node.left = None
            
            elif not node.left:
                node.left = node.right
                node.right = None
            
            invert(node.left)
            invert(node.right)
        invert(root)
        return root