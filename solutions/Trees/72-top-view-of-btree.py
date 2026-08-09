'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def topView(self, root):
        # code here
        
        pos_map = dict()
        answer = []
        
        queue = deque()
        queue.append((root,0))
        
        min_pos = float('inf')
        max_pos = float('-inf')
        
        while queue:
            node,pos = queue.popleft()
            
            min_pos = min(min_pos,pos)
            max_pos = max(max_pos,pos)
            
            if pos not in pos_map:
                pos_map[pos] = node.data
            
            if node.left:
                queue.append((node.left,pos-1))
            
            if node.right:
                queue.append((node.right,pos + 1))
        
        for i in range(min_pos,max_pos+1):
            answer.append(pos_map[i])
        return answer