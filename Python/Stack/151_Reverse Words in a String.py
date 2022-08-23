class Solution:
    def reverseWords(self, s: str) -> str:
        stack=s.split(" ")
        stack.reverse()
        stack2=[]
        for c in stack:
            if c!="":
                stack2.append(c)
        return " ".join(stack2)