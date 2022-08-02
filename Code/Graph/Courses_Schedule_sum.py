from collections import deque
from this import d


def print_orders(tasks, prerequisites):

    # TODO: Write your code her
    req=[]
    dic={i:[] for i in range(tasks)}
    degree={i:0 for i in range(tasks)}
    queue=deque()
    for c,p in prerequisites:
        dic[c].append(p)
        degree[p]+=1
    for k in degree:
        if degree[k]==0:
            queue.append(k)
    def dfs(dic,degree,queues,req):
        if queues:
            for v in queues:
                temp=deque(queues)
                temp.remove(v)
                req.append(v)
                for j in dic[v]:
                    degree[j]-=1
                    if degree[j]==0:
                        temp.append(j)
                dfs(dic,degree,temp,req)
                req.remove(v)
                for c in dic[v]:
                    degree[c]+=1
        if len(req)==len(degree):
            print(req)
    dfs(dic,degree,queue,req)

def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
