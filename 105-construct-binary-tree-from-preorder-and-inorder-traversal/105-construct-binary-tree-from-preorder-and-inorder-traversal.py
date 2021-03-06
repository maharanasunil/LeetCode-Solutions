# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # print(preorder, inorder)
        if len(inorder) == 0: #1
            return None
        
        if len(preorder) == 1: #2
            return TreeNode(preorder[0])
        
        ind = inorder.index(preorder.pop(0)) #3
        node = TreeNode(inorder[ind])
        
        node.left = self.buildTree(preorder, inorder[:ind]) #4
        node.right = self.buildTree(preorder, inorder[ind+1:]) #5
     
        return node