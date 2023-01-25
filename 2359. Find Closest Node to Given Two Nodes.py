class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        d1 = collections.defaultdict(lambda : 100001)
        d2 = collections.defaultdict(lambda : 100001)

        def traversal(root, d):
            stack = [[root,0]]

            while stack:
                node, distance = stack.pop()

                if node not in d:
                    if edges[node] != -1 : stack.append([edges[node], distance+1])
                    d[node] = distance
        
        
        traversal(node1, d1)
        traversal(node2, d2)

        #print(d1, d2)

        min_dist = 100001
        min_node = -1

        for i in range(len(edges)):
            if min_dist > max(d1[i], d2[i]):
                min_dist = max(d1[i], d2[i])
                min_node = i
        return min_node
