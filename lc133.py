#Graphs
#Leetcode 133
# Difficulty: Medium
# Time Complexity: O(e+v) => O(n)
# Space Complexity: O(n) => n = # of vertices in the graph

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        return dfs(node) if node else None