class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #topological
        req=[]
        prevMap={i:[]for i in range(numCourses)}
        for crs,prev in prerequisites:
            prevMap[crs].append(prev)
        #check the deepest element
        #visited
        #visiting added to cycle
        #unvisited not both
        visit=set()
        cycle=set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for prev in prevMap[crs]:
                if not dfs(prev):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            req.append(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return req