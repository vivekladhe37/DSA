class Twitter:

    def __init__(self):
        self.followers_dict = defaultdict(set)
        self.tweets_dict = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.tweets_dict[userId].append((self.counter, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followers_dict[userId] | {userId}
        maxHeap = []
        resultTweetList = []

        for user in users:
            if self.tweets_dict[user]:
                idx = len(self.tweets_dict[user]) - 1
                counter, tweetId = self.tweets_dict[user][idx]
                heapq.heappush(maxHeap, (-counter, tweetId, user, idx))
            
        while maxHeap and len(resultTweetList) < 10:
            counter, tweetId, user, idx = heapq.heappop(maxHeap)
            resultTweetList.append(tweetId)

            if idx > 0:
                idx -= 1
                counter, tweetId = self.tweets_dict[user][idx]
                heapq.heappush(maxHeap, (-counter, tweetId, user, idx))

        return resultTweetList
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers_dict[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers_dict[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)