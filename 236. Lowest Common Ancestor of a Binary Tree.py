# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node):
            if node in (None, p, q): return node
            left, right = helper(node.left), helper(node.right)
            return node if left and right else left or right
        
        return helper(root)

            

            
