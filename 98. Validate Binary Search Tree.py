# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []
        
        def helper(node):
            if not node.left and not node.right: nodes.append(node.val); return
            if node.left: helper(node.left)
            nodes.append(node.val)
            if node.right: helper(node.right) 
        
        helper(root)
        return nodes == sorted(nodes) and len(nodes) == len(set(nodes))