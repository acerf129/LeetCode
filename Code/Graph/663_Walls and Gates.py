from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        rows,cols=len(rooms),len(rooms[0])
        visit=set()
        queue=collections.deque()
        def addRoom(r,c):
            if r<0 or c<0 or r==rows or c==cols or (r,c) in visit or rooms[r][c]==-1:
                return
            visit.add((r,c))
            queue.append([r,c])
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c]==0:
                    queue.append([r,c])
                    visit.add((r,c))
        distance=0
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                rooms[r][c]=distance
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            distance+=1
        