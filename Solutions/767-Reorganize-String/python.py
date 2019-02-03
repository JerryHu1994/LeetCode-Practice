class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        c = collections.Counter(S)
        total_len = len(S)
        sorted_keys = c.most_common()
        maxkeys = sorted_keys[0][1]
        if maxkeys > len(S)-maxkeys+1:  return ""  # return empty string
        heap = [(-p[1], p[0]) for p in sorted_keys]
        heapq.heapify(heap)
        ret = ""
        while len(heap):
            curr = heapq.heappop(heap)
            if len(ret) == 0 or curr[1] != ret[-1]:
                if curr[0]+1 != 0:
                    heapq.heappush(heap, (curr[0]+1, curr[1]))
                ret += curr[1]
            else:
                second = heapq.heappop(heap)
                ret += second[1]
                if second[0]+1 != 0:
                    heapq.heappush(heap, (second[0]+1, second[1]))
                heapq.heappush(heap, curr)
        return ret