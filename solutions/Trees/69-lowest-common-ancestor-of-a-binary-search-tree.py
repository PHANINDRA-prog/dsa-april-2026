class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return None
        
        while root:
            if p.val < root.val and q.val< root.val:
                root = root.left
            
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            else:
                return root