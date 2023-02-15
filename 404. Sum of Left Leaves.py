# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def left_helper(node):
            if not node: return 0 
            if not node.left and not node.right : return node.val
            return left_helper(node.left) + right_helper(node.right)

        def right_helper(node):
            if not node: return 0 
            return left_helper(node.left) + right_helper(node.right)
    
        return right_helper(root)

