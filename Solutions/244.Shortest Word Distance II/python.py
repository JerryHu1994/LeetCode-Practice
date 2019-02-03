class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic = {}
        for i,w in enumerate(words):
            if w in self.dic:
                self.dic[w].append(i)
            else:
                self.dic[w] = [i]
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1 = self.dic[word1]
        list2 = self.dic[word2]
        curr1, curr2 = 0, 0
        ret = float("inf")
        while curr1 < len(list1) and curr2 < len(list2):
            ret = min(abs(list1[curr1]-list2[curr2]), ret)
            if list1[curr1] > list2[curr2]:
                curr2+=1
            else:
                curr1+=1
        
        return ret

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)