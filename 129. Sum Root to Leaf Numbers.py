# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def helper(node, num):
            if not node.left and not node.right : self.ans += num
            if node.left : helper(node.left, num * 10 + node.left.val)
            if node.right : helper(node.right, num * 10 + node.right.val)

        helper(root, root.val)
        return self.ans