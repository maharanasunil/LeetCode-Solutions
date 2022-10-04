# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    #def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    	deq = deque()
    	deq.append((root, sum))
    	while deq:
    		node, curr_sum = deq.popleft()
    		if not node:
    			continue
    		if not node.left and not node.right and curr_sum == node.val:
    			return True
    		deq.append((node.left, curr_sum - node.val))
    		deq.append((node.right, curr_sum - node.val))
    	return False