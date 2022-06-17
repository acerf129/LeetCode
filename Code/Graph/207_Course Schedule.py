class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap={i:[] for i in range(numCourses)}
        visit=set()
        for crs,prev in prerequisites:
            prevMap[crs].append(prev)
        
        def dfs(crs):
            if crs in visit:
                return False
            if prevMap[crs]==[]:
                return True
            visit.add(crs)
            
            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            prevMap[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True