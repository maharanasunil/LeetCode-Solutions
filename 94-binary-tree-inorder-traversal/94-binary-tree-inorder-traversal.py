# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        # root starts out False because you haven't visited it yet
        stack = [(root, False)]
        
        while stack:
            # pop the last element
            node, visited = stack.pop() 
            if node:
                if visited:
                    res.append(node.val)
                else:  
                    # inorder: left -> root -> right
                    # switch because stacks work backwards
                    stack.append((node.right, False)) # has not been visited before
                    stack.append((node, True)) # has been visited before
                    stack.append((node.left, False)) # has not been visited before 
        return res