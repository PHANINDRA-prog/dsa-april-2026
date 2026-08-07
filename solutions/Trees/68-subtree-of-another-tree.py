# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p,q):
            if not p and not q :
                return True
            
            if not p or not q:
                return False
            
            left = same(p.left,q.left)
            right = same(p.right,q.right)

            current = (p.val == q.val)

            return (left and right and current)
        
        def subTree(node,subRoot):
            if not node:
                return False
            
            if node.val == subRoot.val:
                if same(node,subRoot):
                    return True
            
            if subTree(node.left,subRoot):
                return True
            if subTree(node.right,subRoot):
                return True
            return False
        return subTree(root,subRoot)