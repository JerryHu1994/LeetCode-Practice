class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followdic = {}
        self.tweetdict = {}
        self.time = 0
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.tweetdict:
            self.tweetdict[userId] = [(tweetId, self.time)]
        else:
            self.tweetdict[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        listoftws = []
        users = [userId]
           
        if userId in self.followdic:
            users += list(self.followdic[userId])
        # append twts
        for user in users:
            if user in self.tweetdict:
                listoftws.append(copy.copy(self.tweetdict[user]))
        count = 10
        currtwt = None
        currtwttime = -1
        ret = []
        for i in range(10):
            for ind, li in enumerate(listoftws):
                if len(li) == 0:    continue
                if li[-1][1] > currtwttime:
                    currtwt = ind
                    currtwttime = li[-1][1]
            if currtwt==None:
                break
            ret.append(listoftws[currtwt].pop()[0])
            currtwt = None
            currtwttime = -1
        return ret

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        if followerId not in self.followdic:
            self.followdic[followerId] = set([followeeId])
        else:
            self.followdic[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.followdic:
            return
        if followeeId not in self.followdic[followerId]:
            return
        else:
            self.followdic[followerId].remove(followeeId)
            return

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)