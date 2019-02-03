class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff = [gas[i] - cost[i]    for i in range(len(gas))]
        for i in range(len(diff)):
            currsum = 0
            count = 0
            for j in diff[i:] + diff[:i]:
                currsum += j
                if currsum < 0:
                    break
                count += 1
            if count == len(diff):  return i
        return -1
            
# O(n) solution
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost) > sum(gas):    return -1
        n = len(gas)
        diff = [gas[i]-cost[i] for i in range(n)]
        start, end = 0, n-1
        s = diff[start]
        while end > start:
            if s >= 0:
                start += 1
                s += diff[start]
            else:
                s += diff[end]
                end -= 1
        return (start+1)%n if s >= 0 else -1