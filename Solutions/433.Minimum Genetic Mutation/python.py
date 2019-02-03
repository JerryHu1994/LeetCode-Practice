class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        if end not in bank: return -1
        if len(start) != len(end):  return -1
        queue = [start]
        l = len(start)
        ans = 0
        while len(queue):
            currsize = len(queue)
            while currsize > 0:
                currstring = queue.pop(0)
                if currstring == end:   return ans
                currsize -= 1
                for i in range(l):
                    for c in ["A", "C", "G", "T"]:
                        if currstring[i] == c:  continue
                        nextstring = currstring[:i]+c+currstring[i+1:]
                        if nextstring in bank:
                            bank.remove(nextstring)
                            queue.append(nextstring)
            ans += 1
        return -1