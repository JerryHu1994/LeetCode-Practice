class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j < len(words) and i < len(words[j]):
                    if words[i][j] != words[j][i]:
                        return False
                else:
                    return False
        return True