import math
import datetime
import heapq
class ListNode:
    def __init__(self,weight,lasttime,key,val):
        self.key=key
        self.val=val
        self.weight=weight
        self.lasttime=lasttime
        self.score=0
class setCache:
    #get key=O(1) in cache or -1
    #put reach capacity invalidate the least one 
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.nodelist=[]
        self.cache={}
    def getDate(self):
        return datetime.datetime.now()

    def updateScore(self,node):
        dates=self.getDate()       
        node.score=node.weight/(math.log((dates-node.lasttime).microseconds+1))
        node.lasttime=dates

    def get(self,key):
        if key not in self.cache:
            return -1
        #update score and lasttime get value in cache O(1)
        node=self.cache[key]
        self.updateScore(node)
        return node.val

    def put(self,key,value,weight):
        #initial the score
        if key not in self.cache:
            node=ListNode(weight,self.getDate(),key,value)
            node.score=weight/-100
            self.nodelist.append(key)
            self.cache[key]=node
        else:
            #update score and lasttime
            node=self.cache[key]
            self.updateScore(node)
        #delete the least score node 
        # time complexity O(n) for put
        if len(self.cache)>self.capacity:
            key=0
            for k,v in sorted(self.cache.items(),key=lambda x:x[1].score):
                key=k
                break
            del self.cache[key]
            self.nodelist.remove(key)
# with doubly hashmap 
# put if the len(cache)>capacity: discard the least one node

cache=setCache(2)
cache.put(1,1,9)
cache.put(2,2,2)
node=cache.get(1)
#print("node1",node)
cache.put(3,3,2)
node=cache.get(2)
#print("node2",node)
cache.put(4,4,1)
node=cache.get(1)
##print("node1",node)
node=cache.get(3)
#print("node3",node)
node=cache.get(4)
#print("node4",node)
#for k,v in cache.cache.items():
    #print(k,v.score)