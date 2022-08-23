class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None

class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        
        #Left==LRU right=most recent used
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    #remove from left
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev
    #insert from right
    def insert(self,node):
        lefts,rights=self.right.prev,self.right
        lefts.next,rights.prev=node,node
        node.next,node.prev=rights,lefts
    def get(self, key: int) -> int:
        if key in self.cache:
            #TODO update most frequent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])            
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity:
            lru=self.left.next
            del self.cache[lru.key]
            self.remove(lru)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)