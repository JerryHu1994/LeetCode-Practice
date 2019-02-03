class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret, hashmap = [], {}
        for i in strs:
            sortstr = ''.join(sorted(i))
            if sortstr in hashmap:
                hashmap[sortstr].append(i)
            else:
                hashmap[sortstr] = [i]
        for i in hashmap:
            ret.append(hashmap[i])
        return ret
        