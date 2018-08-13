class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):  return False
        dic = collections.defaultdict(list)
        for i in pairs:
            dic[i[0]].append(i[1])
            dic[i[1]].append(i[0])
        for ind, word in enumerate(words1):
            if not (words2[ind] == word or words2[ind] in dic[word]):
                return False
        return True