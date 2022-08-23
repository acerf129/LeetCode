class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rows=len(board)
        if rows<=2:
            return 1
        board.reverse()
        def intoPos(squares):
            r=(squares-1)//rows
            c=(squares-1)%rows
            if r%2:
                c=rows-1-c
            return [r,c]
        
        queue=deque()
        queue.append([1,0])#val,move
        visit=set()
        
        
        while queue :
            val,move=queue.popleft()
            for i in range(1,7):
                nextval=val+i
                r,c=intoPos(nextval)
                if board[r][c]!=-1:
                    nextval=board[r][c]
                if nextval==rows*rows:
                    return move+1
                if nextval not in visit:
                    visit.add(nextval)
                    queue.append([nextval,move+1])
        return -1