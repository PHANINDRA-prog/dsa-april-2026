# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = defaultdict(int)

        for i,num in enumerate(inorder):
            inorder_map[num] = i

        
        def build(pre_left,pre_right,in_left,in_right):
            if pre_left > pre_right:
                return None
            
            root = TreeNode(preorder[pre_left])
            root_index = inorder_map[root.val]
            left_size = root_index - in_left

            root.left = build(pre_left + 1,pre_left + left_size,in_left,in_left + left_size - 1)
            root.right = build(pre_left+left_size+1,pre_right,in_left+left_size+1,in_right)

            return root
        return build(0,len(preorder)-1,0,len(inorder)-1)


