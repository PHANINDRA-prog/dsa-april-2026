# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque,defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        queue.append((root,0,0))

        answer = []

        column_level = defaultdict(list)
        
        while queue:
            node,col,row = queue.popleft()

            column_level[col].append((row,node.val))

            if node.left:
                queue.append((node.left,col-1,row + 1))
            if node.right:
                queue.append((node.right,col + 1,row + 1))
        
        for col in sorted(column_level):
            sorted_nodes = sorted(column_level[col])
            col_values = [val for row,val in sorted_nodes]
            answer.append(col_values)
        return answer