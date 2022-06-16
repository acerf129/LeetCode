class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None
        dic={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
            }
        req=[]
        part=[]
        def backtrack(i):
            if i==len(digits):
                strpart="".join(part)
                req.append(strpart)
                return
            
            val=digits[i]# 2 3
            
            for j in range(len(dic[val])):#abc 3
                part.append(dic[val][j])
                backtrack(i+1)
                part.pop()   
            return 
        backtrack(0)
        return req