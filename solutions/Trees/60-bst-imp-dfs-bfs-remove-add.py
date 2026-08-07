from collections import deque
class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
    
def dfsprintNode(node):
    if not node:
        return
    
    print(node.val)
    dfsprintNode(node.left)
    dfsprintNode(node.right)

def bfsprintNode(node):
    queue = deque()
    queue.append(node)
    answer = []
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        answer.append(current_level)
    print(answer)

def add(node,target):
    if not node:
        return TreeNode(target)
    
    if target < node.val:
        node.left = add(node.left,target)
    
    else:
        node.right = add(node.right,target)
    
    return node

def remove(node,target):
    if not node:
        return None

    if target < node.val:
        node.left = remove(node.left,target)
    
    elif target > node.val:
        node.right = remove(node.right,target)
    
    else:
        # leaf node:
        if not node.left and not node.right:
            return None
        
        # One child:
        if not node.right:
            return node.left
        
        if not node.left:
            return node.right
        
        # Two child
        # Find successor
        successor = node.right

        # Find the inorder successor
        # (leftmost node of the right subtree).
        # It is the smallest value greater than the current node,
        # so replacing the current node with it preserves the BST property.
        while successor.left:
            successor = successor.left
        
        node.val = successor.val

        node.right = remove(node.right,successor.val)
    return node



root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(7)
root.right.right = TreeNode(8)

dfsprintNode(root) # Preorder priniting
bfsprintNode(root) # BFS Order printing
new_root = add(root,9)
bfsprintNode(new_root)
new_root = remove(root,3)
bfsprintNode(new_root)









