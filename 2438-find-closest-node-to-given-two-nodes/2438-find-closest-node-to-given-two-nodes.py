class Solution:
    def buildDistPath(self, edges, node, path):
        while edges[node] != -1:
            prev = node
            node = edges[node]
            if node in path:
                break
            path[node] = path[prev] + 1

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        path1 = {node1:0}
        self.buildDistPath(edges, node1, path1)
        path2 = {node2:0}
        self.buildDistPath(edges, node2, path2)

        min_dist = float('inf')
        node_idx = n
        for node in path1:
            if node in path2:
                max_dist = max(path1[node], path2[node])
                if max_dist == min_dist:
                    node_idx = min(node_idx, node)
                elif max_dist < min_dist:
                    min_dist = max_dist
                    node_idx = node
        
        return node_idx if min_dist != float('inf') else -1
        
        