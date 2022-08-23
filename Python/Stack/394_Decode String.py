class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        temp=""
        count=""
        req=""
        for c in s:
            if c=="]":
                while stack and  not stack[-1].isdigit():
                    val=stack.pop()
                    if val!="[":
                        temp=val+temp
                while stack and stack[-1].isdigit():                    
                    val=stack.pop()
                    count=val+count
                stack.append(int(count)*temp)
                temp=""
                count=""
            else:
                stack.append(c)
        return "".join(stack)