def recur(n, cur): 
    n2=int(n)
    #1.5 error 2.5 pass
    if n2!=n or n2<2:
        raise Exception("Invalid input")    

    #now n2==n
    for i in range(n2,1,-1):
        if not cur:
            cur=0
        #print(n,cur)
        if n==2:
            return 1/n+cur
        cur=cur + 1 / (n * (n -1))
        n=n-1

#print(recur(10.5,30))       
#print(recur(2.5,30))
#print(recur(20,50))