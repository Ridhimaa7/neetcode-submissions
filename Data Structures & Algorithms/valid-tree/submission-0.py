from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashmap = defaultdict(list)
        visited = set()
        for val in edges:
            hashmap[val[0]].append(val[1])
            hashmap[val[1]].append(val[0])
        def dfs(node,visited,parent_node):
            visited.add(node)
            for neighbour in hashmap[node]:
                if neighbour == parent_node:
                    continue
                if neighbour in visited:
                    return False
                if not dfs(neighbour, visited,node):
                    return False
            return True
        return dfs(0, visited, -1) and len(visited) == n
        
        