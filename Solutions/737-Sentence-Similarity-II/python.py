class Solution(object):
    def dfs(self, dic, word1, word2):
        s = set()
        stack = [word1]
        while len(stack):
            curr = stack.pop()
            s.add(curr)
            simwords = dic[curr]
            if word2 in simwords:
                return True
            for w in simwords:
                if w not in s:
                    stack.append(w)
        return False
            
    
    def areSentencesSimilarTwo(self, words1, words2, pairs):
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
            if not (words2[ind] == word or self.dfs(dic, word, words2[ind])):
                return False
        return True