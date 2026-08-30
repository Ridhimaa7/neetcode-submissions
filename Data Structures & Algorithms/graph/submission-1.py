class Graph:
    
    def __init__(self ):
        self.adjlist = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src in self.adjlist:
            self.adjlist[src].add(dst)
        else:
            self.adjlist[src] = {dst}
        if dst not in self.adjlist:
            self.adjlist[dst] = set()



    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjlist:
            if dst in self.adjlist[src]:
                self.adjlist[src].remove(dst)
                return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        def dfs(node , target , visited ):
            if node == target:
                return True
            if node in visited:
                return False
            visited.add(node)
            for n in self.adjlist.get(node , []):
                if n in visited:
                    continue
                if dfs(n , target , visited):
                    return True
            return False
        return dfs(src , dst , set())
            

