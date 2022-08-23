class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sums=sum(matchsticks)
        if sums %4:
            return False
        target=sums//4        
        req=[]
        used=[False]*len(matchsticks)
        dic={}
        def backtrack(cur,t,ith):
            if t==4:
                return True
            if cur>target:
                return False
            if (cur,ith)in dic:
                return dic[(cur,ith)]
            
            if cur==target:
                dic[(cur,ith)]=backtrack(0,t+1,ith)
                return dic[(cur,ith)]
            
            for i in range(len(matchsticks)):
                if not used[i] and cur+matchsticks[i]<=target:
                    used[i]=True
                    temp=ith
                    ith=ith|1<<i
                    req=backtrack(cur+matchsticks[i],t,ith)
                    if req:
                        dic[(cur,ith)]=True
                        return True
                    ith=temp
                    used[i]=False
            dic[(cur,ith)]=False
            return False
        
        return backtrack(0,0,0)

        sums=sum(matchsticks)
        if sums%4 or not matchsticks:
            return False
        target=sums//4
        matchsticks.sort(reverse=True)
        sums=[0 for _ in range(4)]
        
        def dfs(index):
            if index==len(matchsticks):
                return sums[0]==sums[1]==sums[2]==target
            for i in range(4):
                if sums[i]+matchsticks[index]<=target:
                    sums[i]+=matchsticks[index]
                    if dfs(index+1):
                        return True
                    sums[i]-=matchsticks[index]
            return False    
        return dfs(0)