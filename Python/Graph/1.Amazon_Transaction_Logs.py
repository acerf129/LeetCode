def processLogs(logs, threshold):
    # Write your code here
    dic={}
    for i in range(len(logs)):
        lis=logs[i].split(" ");
        dic[lis[0]]=dic.get(lis[0],0)+1
        if lis[0]!=lis[1]:
            dic[lis[1]]=dic.get(lis[1],0)+1
    req=[]
    for c in (dic.items()):
        if c[1]>=threshold:
            req.append(int(c[0]))
    req.sort()
    res=[str(x)for x in req]
    return res