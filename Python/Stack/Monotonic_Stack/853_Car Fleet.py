class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        stack=[]
        for p,s in sorted(pair)[::-1]:
            #target-position /s
            stack.append((target-p)/s)
            print(stack)
            # time smaller means faster
            #remove faster
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                    stack.pop()
        return len(stack)