# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        q = deque([root])

        currdepth = 1

        while q and currdepth + 1 != depth:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            currdepth +=1
        
        for node in q:
            node.left, node.left.left = TreeNode(val), node.left
            node.right, node.right.right = TreeNode(val), node.right
        
        return root
        


        





        