class Twitter:

    def __init__(self):
        self.time=0
        self.tweetMap=defaultdict(list)#userID time,tweetid
        self.followMap=defaultdict(set)#userID

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time,tweetId])
        self.time-=1
    def getNewsFeed(self, userId: int) -> List[int]:
        req=[]
        minHeap=[]
        self.followMap[userId].add(userId)
        for follow in self.followMap[userId]:
            if follow in self.tweetMap:
                index=len(self.tweetMap[follow])-1
                time,tweetId=self.tweetMap[follow][index]
                minHeap.append([time,userId,tweetId,follow,index-1])
        heapq.heapify(minHeap)
        while minHeap and len(req)<10:
            time,userId,tweetId,follow,index=heapq.heappop(minHeap)
            req.append(tweetId)
            if index>=0:
                time,tweetId=self.tweetMap[follow][index]
                heapq.heappush(minHeap,[time,userId,tweetId,follow,index-1])
        return req
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)