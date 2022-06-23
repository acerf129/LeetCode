class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit=[]
        letter=[]
        for l in logs:
            split=l.split()
            if len(split)>1 and split[1].isdigit():
                digit.append(l)            
            else:
                letter.append(l)
        
        letter.sort(key=lambda x:(x[x.find(" ")+1:],x[:x.find(" ")+1]   ))
        
        return letter+digit