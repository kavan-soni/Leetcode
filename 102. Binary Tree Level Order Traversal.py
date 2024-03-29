# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        levels = set()

        def helper(node, level):
            if not node: return
            if level not in levels: ans.o([node.val]); levels.add(level)
            else: ans[level].append(node.val)
            helper(node.left, level+1)
            helper(node.right, level+1)


        helper(root,0)
        return ans