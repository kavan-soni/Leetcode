# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

    
        def tuplify(root):
            if root:
                tuple = root.val, tuplify(root.left), tuplify(root.right)
                trees[tuple].append(root)
                return tuple
        trees = collections.defaultdict(list)
        tuplify(root)
        return [roots[0] for roots in trees.values() if roots[1:]]
    '''

        def isDuplicateTree(node1, node2):
            # check if two trees are duplicate
            
            q1, q2 = [node1], [node2]

            while q1 and q2:
                n1, n2 = q1.pop(0), q2.pop(0)

                if not n1 and not n2 : continue
                if not n1 or not n2 or n1.val != n2.val : return False

                q1.append(n1.left); q1.append(n1.right)
                q2.append(n2.left); q2.append(n2.right)
            
            return False if q1 or q2  else True
            

        def checkForDuplicate(node_root):
            #check all nodes of tree to find any duplicates
            if node_root in ans: return
            q = [root]
            while q :
                n = q.pop(0)
                if not n : continue
                
                if n.val == node_root.val and n != node_root and isDuplicateTree(n, node_root):
                    ans.append(node_root)
                    break
                
                q.append(n.left); q.append(n.right)
            
            return
 
        ans = list()

        # traverse every node of tree
        q = [root]
        while q :
            node = q.pop(0)
            if not node : continue
            checkForDuplicate(node)
            q.append(node.left); q.append(node.right)
        
        return ans

    '''

            
