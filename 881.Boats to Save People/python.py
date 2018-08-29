class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people, ret = sorted(people), 0
        left, right = 0, len(people)-1
        while left <= right:
            if people[right] + people[left] > limit:
                right -= 1
                ret += 1
            else:
                left += 1
                right -= 1
                ret += 1
        return ret
                