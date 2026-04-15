import heapq 
class Twitter:
    def __init__(self):
        self.time = 0
        self.uToT = dict()
        self.uToF = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.uToF:
            self.uToF[userId] = set([userId])
        if userId not in self.uToT:
            self.uToT[userId] = []
        heapq.heappush(self.uToT[userId], (self.time, tweetId))
        while len(self.uToT[userId]) > 10:
            heapq.heappop(self.uToT[userId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for f in self.uToF[userId]:
            for t in self.uToT[f]:
                heapq.heappush(feed, (-t[0], t[1]))
        
        ret = []
        for i in range(10):
            if len(feed) == 0:
                break
            ret.append(heapq.heappop(feed)[1])
        return ret
            
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.uToF:
            self.uToF[followerId] = set()
        self.uToF[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followerId in self.uToF and followeeId in self.uToF[followerId]:
            self.uToF[followerId].remove(followeeId)
