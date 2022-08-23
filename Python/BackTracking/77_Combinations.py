class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        count=Counter([i for i in range(1,n+1)])
        req=[]
        cur=[]
        def backtrack(i,count):
            if i==k:
                req.append(cur.copy())   
                return req
            
            for c in count:
                if count[c]>0:
                    if not cur or (cur and c>cur[-1]):
                        count[c]-=1
                        cur.append(c)
                        backtrack(i+1,count)
                        cur.pop()
                        count[c]+=1
            return 
        backtrack(0,count)
        
        return req

        req=[]
        
        def backtrack(i,cur):
            if len(cur)==k:
                req.append(cur.copy())
                return
            for j in range(i,n+1):
                cur.append(j)
                backtrack(j+1,cur)
                cur.pop()
            
        backtrack(1,[])
        return req