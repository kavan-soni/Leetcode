# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(node, remainder):
            if not node: return 0
            if not node.left and not node.right: return remainder == node.val
            return helper(node.left, remainder-node.val) or helper(node.right, remainder-node.val)

        return helper(root, targetSum)
