# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node, s):
            ans_str = s + "->" + str(node.val)

            if not node.left and not node.right: 
                if ans_str not in ans: ans.append(ans_str[2:])
                return
            
            if node.left: dfs(node.left, ans_str)
            if node.right: dfs(node.right, ans_str)





        dfs(root, "")
        return ans