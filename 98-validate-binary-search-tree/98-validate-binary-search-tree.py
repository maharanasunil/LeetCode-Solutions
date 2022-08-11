# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tree = []
     
    def inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.inorder(root.left);
        self.tree.append(root.val);
        self.inorder(root.right);
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not root.right and not root.left:
            return True
        
        self.inorder(root)
        
        for i in range(len(self.tree) - 1):
            if self.tree[i] >= self.tree[i + 1]:
                return False
        return True;