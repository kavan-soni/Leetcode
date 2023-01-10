# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        q1 = [root.left]
        q2 = [root.right]

        while q1 and q2:

            n1 = q1.pop(0)
            n2 = q2.pop(0)

            if not n1 and not n2: continue
            if not n1 or not n2: return False
            if n1.val != n2.val: return False

            q1.append(n1.left)
            q1.append(n1.right)

            q2.append(n2.right)
            q2.append(n2.left)
        
        return True

