class TweetCounts:

    def __init__(self):
        self.count_dic = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.count_dic[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        ans = []
        sorted_times = sorted(self.count_dic[tweetName])
        time_fre = 0
        if freq == "minute":
            time_fre = 60
        elif freq == "hour":
            time_fre = 3600
        elif freq == "day":
            time_fre = 86400
        curr_cnt = 0
        curr_start = startTime
        ind = 0
        while curr_start <= endTime:
            if ind < len(sorted_times):
                if sorted_times[ind] >= curr_start and sorted_times[ind] < min(endTime+1, curr_start+time_fre):
                    curr_cnt += 1
                    ind += 1
                elif sorted_times[ind] < curr_start or sorted_times[ind] > endTime:
                    ind += 1
                    continue
                elif sorted_times[ind] >= curr_start+time_fre:
                    ans.append(curr_cnt)
                    curr_start += time_fre
                    curr_cnt = 0
            else:
                ans.append(curr_cnt)
                curr_start += time_fre
                curr_cnt = 0
        return ans

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)