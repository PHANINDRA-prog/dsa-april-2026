# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def remove(node,target):
            if not node:
                return None
            
            if target < node.val:
                node.left = remove(node.left,target)
            
            elif target > node.val:
                node.right = remove(node.right,target)
            
            else:

                # Leaf Node
                if not node.left and not node.right:
                    return None
                
                # One child Node
                if not node.left:
                    return node.right 
                
                if not node.right:
                    return node.left
                
                # Two child Node
                successor = node.right

                while successor.left:
                    successor = successor.left
                
                # Now we have the successor who is the min value in the entire right subtree 

                node.val = successor.val

                node.right = remove(node.right,successor.val)
            return node
        return remove(root,key)