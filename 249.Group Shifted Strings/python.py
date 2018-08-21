class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        for s in strings:
            firstc = s[0]
            encode = ["0"]
            for c in s[1:]:
                diff = ord(c) - ord(firstc)
                if diff < 0:    diff += 26
                encode.append(str(diff))
            key = ".".join(encode)
            dic[key].append(s)
        return [v for v in dic.values()]