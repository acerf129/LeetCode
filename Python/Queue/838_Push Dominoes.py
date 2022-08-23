class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom=list(dominoes)
        q=deque()
        for i,v in enumerate(dom):
            if v!=".":
                q.append((i,v))
        while q :
            index,value=q.popleft()
            if value=="L":
                if index>0 and dom[index-1]==".":
                    q.append((index-1,"L"))
                    dom[index-1]="L"
            else:
                if index+1<len(dom)and dom[index+1]==".":
                    if index+2<len(dom)and dom[index+2]=="L":
                        q.popleft()#cause next is L
                    else :
                        q.append((index+1,"R"))
                        dom[index+1]="R"                   
        return "".join(dom)