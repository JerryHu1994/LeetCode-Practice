class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.dic = collections.defaultdict(list)
        self.winners = []
        self.times = times
        curr, currw = 0, None
        for i in range(len(persons)):
            p, t = persons[i], times[i]
            self.dic[p].append(t)
            if len(self.dic[p]) >= curr:
                curr = len(self.dic[p])
                currw = p
            self.winners.append(currw)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        pos = bisect.bisect_right(self.times, t)
        return self.winners[pos-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)