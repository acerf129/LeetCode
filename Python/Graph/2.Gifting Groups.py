def countGroups(related):
    # Write your code here
    dic={}
    for i in range(len(related)):
        dic[i]=[[],False]
        for j in range(len(related)):
            if i==j:
                continue
            if related[i][j]=="1":
                dic[i][0].append(j)
    def dfs(num):
        if dic[num][1]==True:
            return 
        dic[num][1]=True
        if dic[num][0]==[]:
            return
        for k in dic[num][0]:
            dfs(k)
    req=0
    for n in range(len(dic)):
        if dic[n][1]==False:
            dfs(n)
            req+=1
    return req