class Solution:
    def longestValidParentheses(self, s: str) -> int:
        req=0
        stack=[]
        stack.append(-1)
        for i,c in enumerate(s):
            if c=="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    req=max(req,i-stack[-1])
        return req

    
        for i in range(1,len(s)):
            if s[i]==")":
                if s[i-1]=="(":
                    dp[i]=dp[i-2]+2 if i>=2 else 2
                elif i-dp[i-1]-1>=0 and  s[i-dp[i-1]-1]=="(" :
                    #dp= dp[i]-1+2+ the first dp before the (
                    dp[i]=dp[i-1]+(dp[i-dp[i-1]-2]if i-dp[i-1]>=2 else 0)+2
                
                req=max(req,dp[i])
        return req