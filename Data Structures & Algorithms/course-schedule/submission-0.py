class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if thereis a cycle in graph means return False
        adjList = {i: [] for i in range(numCourses)}
        for src , dest in prerequisites:
            adjList[src].append(dest)
        visited = set()
        safe = set()
        def dfs(node):
            if node in visited:
                return False
            if node in safe:
                return True
            visited.add(node)
            for neighbours in adjList[node]:
                if not dfs(neighbours):
                    return False
            visited.remove(node)
            safe.add(node)
            return True
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True