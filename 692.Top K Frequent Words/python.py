class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        heaplist = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heaplist)
        return [heapq.heappop(heaplist)[1] for _ in xrange(k)]